import discogs_client as dc
import random
from discogs_client.exceptions import HTTPError

ds = dc.Client('ExampleApplication/1.0', user_token='nIQEQwJRVUVrMosdXxiaOJTOhtflqWPhRWyNKgGo')

numberofnames = input('How many names do you want? ')

print('OK. Printing', numberofnames, ' names...\n')

i = 0;
while i < int(numberofnames):
#for i in range(int(numberofnames)):
	rannum = random.randrange(1, 9394202)
	therelease = ds.release(rannum)
	try:
		#if len(therelease.artists) > 1:
			#print('\n(This release has multiple artists)')
		for artist in therelease.artists:
			try:
				print(artist.name)
				i = i+1
			except UnicodeEncodeError:
				print('(----There\'s a character in this artist\'s name that can\'t be printed----)')
	except HTTPError:
		print('(----No release with ID', rannum, '----)')
			
		