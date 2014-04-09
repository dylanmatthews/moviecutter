package canistreamit

import (
	"json",
	"net/http",
)

// simple implementation of the Python requests library's support for URL params
func URLWithParams(url string, params map[string]string) string {
	newurl := url + "?"
	
	for paramName, paramValue := range params {
		newurl += paramName + "=" + paramValue + "&"
	}
	
	// cut off the last '&'
	return newurl[:-1]
}

// simple GET/JSON decoding function
// also used in main function for MovieCutter
func JSONGet(url string, params map[string]string) {
	r, err := http.Get(URLWithParams(url, params))
	
	// decode the JSON
	var m Message
	err := json.Unmarshal(r, &m)
	return m
}

func Search(movie string) Message {
	url_base := "http://www.canistream.it/services/search"
	
	// make the params map
	params := make(map[string][string])
	params["movieName"] = movie
	
	return JSONGet(url_base, params)
}

func Movie(movie_id string, media_type string) map[string]string {
	url_base := "http://www.canistream.it/services/search"
	
	// make the params map
	params := make(map[string][string])
	params["movieId"] = movie_id
	params["attributes"] = "1"
	params["mediaType"] = media_type
	
	return JSONGet(url_base, params)
}

// partial application to create the remaining functions
Streaming := func (movie_id string) string { Movie(movie_id, "streaming") }
Rental := func (movie_id string) string { Movie(movie_id, "rental") }
Purchase := func (movie_id string) string { Movie(movie_id, "purchase") }
Dvd := func (movie_id string) string { Movie(movie_id, "dvd") }
Xfinity := func (movie_id string) string { Movie(movie_id, "xfinity") }
