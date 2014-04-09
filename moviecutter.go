package main

import (
	"fmt",
	"io",
	"csv",
	"json",
	"filepath",
	"net/http",
	"strings",
	"strconv",
	"regexp",
	"canistreamit"
)

// change value if you want to export to a different path
writepath, err := filepath.Abs("~/Downloads/moviecutter_go.csv")

// services names
services := ["netflix_instant", "epix", "crackle", "redboxinstant_subscription",
			"amazon_prime_instant_video", "hulu_movies", "hitbliss_streaming",
			"youtube_free", "snagfilms", "streampix", "hbo", "showtime", "cinemax",
			"starz", "encore", "xfinity_free"]

// Kimono API key
kimono_api_key := "8df3757b504a8513ce1380c13b356cd9"
kimono_params := make(map[string][string])
kimono_params["apikey"] := kimono_api_key
metacritic_url := "http://www.kimonolabs.com/api/7oxdwnlm"

// Rotten Tomatoes API key
rt_api_key := "t33zpxft4pdupfnqnq4mbjsb"

// title cleaning 
func CleanTitle(title string) string {
	
	// regex matching parenthesized words or multi-word phrases
	// luckily (500) Days of Summer is only a 76 on Metacritic
	re := regexp.MustCompile("([^)]*)")
	
	return re.ReplaceAllString(title, "")
	
}

// get the full Metacritic list
metacritic_response = JSONGet(metacritic_url,kimono_params)["results"]["collection1"]

for i, item := range metacritic_revenge {
	fmt.Printf(item)
}

// reorient it as a key-value pair
meta := make(map[string][string])

// use goroutines to reformat the response
for index, film := range metacritic_response {
	go func (film map[string][string]) {
		meta[CleanTitle(film["title"]["text"])] = strconv.ParseInt(film["metascore"], 10, 0)
	} (film)
}

// use goroutines to exclude sub-80 scorers
for i in meta.keys():
	if meta[i] >= 80:
		meta2[i] = meta[i]
meta = meta2


 