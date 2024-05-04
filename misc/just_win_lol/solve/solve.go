package main

import (
	"fmt"
	"math/rand"
	"time"
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
	getLikeliness()

	timeNow := time.Now().UTC().Unix()

	count := 0
	results := make(map[time.Time][]card, 10)
	for count < 10 {
		var r = rand.New(rand.NewSource(timeNow))
		hand := randHand(*r)
		if isFiveOfAKind(hand) {
			results[time.Unix(timeNow, 0)] = hand
			count++
		}
		timeNow++
	}
	fmt.Println(results)
}

func getLikeliness() {
	timeNow := time.Now().UTC().Unix()
	fmt.Println(timeNow)

	count := 0
	results := make([]int64, 100)
	for count < 100 {
		done := false
		origTime := timeNow
		for !done {
			var r = rand.New(rand.NewSource(timeNow))
			hand := randHand(*r)
			if isFiveOfAKind(hand) {
				done = true
			}
			timeNow++
		}
		results[count] = timeNow - origTime
		count++
	}
	fmt.Println(findStats(results))
}

func findStats(slice []int64) (float64, int64, int64) {
	var sum int64
	sum = 0
	min := slice[0]
	max := slice[0]
	for _, element := range slice {
		sum += element
		if element < min {
			min = element
		}
		if element > max {
			max = element
		}
	}
	mean := float64(sum) / float64(len(slice))
	return mean, min, max
}
