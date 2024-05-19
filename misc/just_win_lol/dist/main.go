package main

import (
	"fmt"
	"log"
	"math/rand"
	"net/http"
	"time"

	"github.com/MadAppGang/httplog"
	"github.com/alexedwards/scs/v2"
	"github.com/sethvargo/go-limiter/httplimit"
	"github.com/sethvargo/go-limiter/memorystore"
)

type card struct {
	value string
	suit  string
}

func (c *card) String() string {
	return fmt.Sprintf("%s%s", c.value, c.suit)
}

var cardValues = []string{"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"}
var cardSuits = []string{"h", "c", "d", "s"}
var handSize = 12
var requiredWins = 5
var sessionManager *scs.SessionManager

func randHand(r rand.Rand) []card {
	hand := make([]card, handSize)
	sum := 0
	for sum < handSize {
		hand[sum] = card{
			value: cardValues[r.Intn(len(cardValues))],
			suit:  cardSuits[r.Intn(len(cardSuits))],
		}
		sum++
	}
	return hand
}

func isFiveOfAKind(hand []card) bool {
	counts := make(map[string]int)
	for _, card := range hand {
		element := card.value
		counts[element] = counts[element] + 1
		if counts[element] >= 5 {
			return true
		}
	}
	return false
}

func main() {
	sessionManager = scs.New()
	sessionManager.Lifetime = 20 * time.Minute

	mux := http.NewServeMux()

	mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		if !sessionManager.Exists(r.Context(), "handsRemaining") || !sessionManager.Exists(r.Context(), "wins") {
			log.Println(r.Header["X-Real-Ip"], "new session")
			sessionManager.Put(r.Context(), "handsRemaining", 10)
			sessionManager.Put(r.Context(), "wins", 0)
		}
		handsRemaining := sessionManager.GetInt(r.Context(), "handsRemaining")
		wins := sessionManager.GetInt(r.Context(), "wins")

		// from index.templ
		indexComponent(handsRemaining, wins).Render(r.Context(), w)
	})
	mux.HandleFunc("/hand", func(w http.ResponseWriter, r *http.Request) {
		// current time in unix seconds
		var timeNow = time.Now().UTC().Unix()
		var rand_time = rand.New(rand.NewSource(timeNow))
		hand := randHand(*rand_time)
		log.Println(r.Header["X-Real-Ip"], hand)

		handsRemaining := sessionManager.GetInt(r.Context(), "handsRemaining")
		currentWins := sessionManager.GetInt(r.Context(), "wins")

		if isFiveOfAKind(hand) && sessionManager.GetInt64(r.Context(), "lastWin") < timeNow {
			sessionManager.Put(r.Context(), "lastWin", timeNow)
			currentWins += 1
		}

		if handsRemaining <= 0 {
			handsRemaining = 10
			currentWins = 0
		} else {
			handsRemaining -= 1
		}

		sessionManager.Put(r.Context(), "handsRemaining", handsRemaining)
		sessionManager.Put(r.Context(), "wins", currentWins)

		// from index.templ
		handComponent(hand, handsRemaining, currentWins).Render(r.Context(), w)
	})
	mux.HandleFunc("/status", func(w http.ResponseWriter, r *http.Request) {
		handsRemaining := sessionManager.GetInt(r.Context(), "handsRemaining")
		wins := sessionManager.GetInt(r.Context(), "wins")

		// from index.templ
		sidebarComponent(handsRemaining, wins).Render(r.Context(), w)
	})
	mux.HandleFunc("/reset", func(w http.ResponseWriter, r *http.Request) {
		sessionManager.Put(r.Context(), "handsRemaining", 10)
		sessionManager.Put(r.Context(), "wins", 0)

		// from index.templ
		sidebarComponent(10, 0).Render(r.Context(), w)
	})
	fs := http.FileServer(http.Dir("assets/"))
	mux.Handle("/static/", http.StripPrefix("/static/", fs))

	store, err := memorystore.New(&memorystore.Config{
		// Number of tokens allowed per interval.
		Tokens: 30,

		// Interval until tokens reset.
		Interval: time.Minute,
	})
	if err != nil {
		log.Fatal(err)
	}
	limiterMiddleware, err := httplimit.NewMiddleware(store, httplimit.IPKeyFunc())
	if err != nil {
		log.Fatal(err)
	}

	muxWithSessionMiddleware := httplog.Logger(limiterMiddleware.Handle(sessionManager.LoadAndSave(mux)))

	log.Println("startup")
	log.Fatal(http.ListenAndServe(":8080", muxWithSessionMiddleware))
}
