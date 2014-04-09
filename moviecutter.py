import canistreamit
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
services = ['netflix_instant', 'epix', 'crackle', 'redboxinstant_subscription',
			'amazon_prime_instant_video', 'hulu_movies', 'hitbliss_streaming',
			'youtube_free', 'snagfilms', 'streampix', 'hbo', 'showtime', 'cinemax',
			'starz', 'encore', 'xfinity_free']

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

# structure as a title : score dict
meta = {}
	
for (index, film) in enumerate(metacritic):
	meta[cleantitle(film["title"]["text"])] = int(film["metascore"])

# get rid of under 80 scorers
meta2 = {}
for i in meta.keys():
	if meta[i] >= 80:
		meta2[i] = meta[i]
meta = meta2


# find tomatometer scores for Metacritic/MRQE picks
for k in meta.iterkeys():
	try:
		tomatometer = requests.get('http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=t33zpxft4pdupfnqnq4mbjsb&q='
									+ str(k) + '&page_limit=1').json()["movies"][0]["ratings"]["critics_score"]
		if not "tomatometer" in merged[k]:
			merged[k]["tomatometer"] = tomatometer		
	except:
		continue

print "Tomatometers received\n" + str(datetime.now().time())

print "Checking streaming services; this could take a couple of hours…"

# connect to CanIStreamIt
for i in merged.iterkeys():
	try:
		movie = canistreamit.search(i)[0]['_id']
	except:
		continue
		
	for service in services:
		try:
			if service in canistreamit.streaming(movie):
				merged[i][service] = True
			elif service in canistreamit.xfinity(movie):
				merged[i][service] = True
			else:
				merged[i][service] = False
		except requests.exceptions.ConnectionError:
			continue

print "Stream info received\n" + str(datetime.now().time())

# format for CSV
first = ["name", "metascore", "tomatometer"]
headers = first+services
csvlist = [headers]
for i in merged.iterkeys():
	row = [i]
	for var in headers:
		if var in merged[i]:
			row.append(merged[i][var])	
		else:
			row.append("")
	csvlist.append(row)
	
# write it out
with open(writepath, 'wb') as csvfile:
	writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
	writer.writerows(csvlist)

print "CSV file written"
