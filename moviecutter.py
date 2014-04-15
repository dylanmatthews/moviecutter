import json
import requests
import csv
import re
from unidecode import unidecode
from datetime import datetime
from os.path import expanduser

# set the output file's destination
# AMEND THIS TO CHANGE WHERE OUTPUT WILL GO
writepath = expanduser('~/Downloads/moviecutter.csv')

# streaming services to check
# key names are same as CanIStreamIt? for easier iteration
# services = ['netflix_instant', 'epix', 'crackle', 'redboxinstant_subscription',
#			'amazon_prime_instant_video', 'hulu_movies', 'hitbliss_streaming',
#			'youtube_free', 'snagfilms', 'streampix', 'hbo', 'showtime', 'cinemax',
#			'starz', 'encore', 'xfinity_free']

# simple function for cleaning up titles by removing parens
def cleantitle(title):
	words = title.split()
	
	ret = ""
	for word in words:
		if (word[0]!='(' and word[-1]!=')'):
		 ret += unidecode(word) + ' '
	
	# get rid of last space
	ret = ret[0:-1]
		 
	return ret

# get the full Metacritic list
r = requests.get('http://www.kimonolabs.com/api/7oxdwnlm?apikey=8df3757b504a8513ce1380c13b356cd9')
metacritic = r.json()["results"]["collection1"]

print "Metascores received\n" + str(datetime.now().time())	
print "Checking tomatometer scores and streaming services; this could take a couple of minutes..."

headers = ["name", "metascore", "tomatometer"]
csvlist = [headers]


for (index, film) in enumerate(metacritic):
	score = int(film["metascore"])
	
	# limit to 80+ scorers
	if score>=80:
	
		
		title = cleantitle(film["title"]["text"])
		row = [title]
		row.append(int(film["metascore"]))
		
		# get tomatometer and canistreamit data
		try:
			tomatometer = requests.get('http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=t33zpxft4pdupfnqnq4mbjsb&q='
										+ title + '&page_limit=1').json()["movies"][0]["ratings"]["critics_score"]
			
			row.append(tomatometer)
			
		##	k = requests.get('http://www.canistream.it/services/search', params={'movieName': title}).content
			
		##	movie = canistreamit.search(title)[0]['_id']
		##	print movie
		##	for service in services:
		##		try:
		##			if service in canistreamit.streaming(movie):
		##				row.append("True")
		##			elif service in canistreamit.xfinity(movie):
		##				row.append("True")
		##			else:
		##				row.append("False")
		##		except requests.exceptions.ConnectionError:
		##			continue

		except:
			continue
				
		csvlist.append(row)

print "Tomatometers received\n" + str(datetime.now().time())

	
# write it out
with open(writepath, 'wb') as csvfile:
	writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
	writer.writerows(csvlist)

print "CSV file written"
