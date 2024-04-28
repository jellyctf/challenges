package main

import (
	"log"
	"math/rand"
	"net/http"
	"time"

	"github.com/a-h/templ"
)

var cards = []string{"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"}
var suits = []string{"h", "c", "d", "s"}
var handSize = 12

func randHand(r rand.Rand) []string {
	hand := make([]string, handSize)
	sum := 0
	for sum < handSize {
		hand[sum] = cards[r.Intn(len(cards))]
		sum++
	}
	return hand
}

func isFiveOfAKind(slice []string) bool {
	counts := make(map[string]int)
	for _, element := range slice {
		counts[element] = counts[element] + 1
		if counts[element] >= 5 {
			return true
		}
	}
	return false
}

func main() {
	http.Handle("/", templ.Handler(indexComponent()))
	http.HandleFunc("/hand", func(w http.ResponseWriter, r *http.Request) {
		var rand_time = rand.New(rand.NewSource(time.Now().UTC().Unix()))
		hand := randHand(*rand_time)
		log.Println(r.Header["X-Real-Ip"], hand)
		handComponent(hand).Render(r.Context(), w)
	})
	fs := http.FileServer(http.Dir("assets/"))
	http.Handle("/static/", http.StripPrefix("/static/", fs))

	log.Fatal(http.ListenAndServe(":8080", nil))

	// timeNow := time.Now().UTC().Unix()
	// fmt.Println(timeNow)

	// count := 0
	// results := make([]int64, 100)
	// for count < 100 {
	// 	done := false
	// 	origTime := timeNow
	// 	for !done {
	// 		var r = rand.New(rand.NewSource(timeNow))
	// 		hand := randHand(*r)
	// 		if isFiveOfAKind(hand) {
	// 			done = true
	// 		}
	// 		timeNow++
	// 	}
	// 	results[count] = timeNow - origTime
	// 	count++
	// }
	// fmt.Println(findStats(results))
}

// func findStats(slice []int64) (float64, int64, int64) {
// 	var sum int64
// 	sum = 0
// 	min := slice[0]
// 	max := slice[0]
// 	for _, element := range slice {
// 		sum += element
// 		if element < min {
// 			min = element
// 		}
// 		if element > max {
// 			max = element
// 		}
// 	}
// 	mean := float64(sum) / float64(len(slice))
// 	return mean, min, max
// }
