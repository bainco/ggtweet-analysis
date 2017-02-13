import re
import globes_tweets as gt
import json
import get_award_relationships as rel
import operator 

positives = ['good', 'nice', 'terrific', 'great', 'amazing', 'proud']
negatives = ['bad', 'terrible', 'horrific', 'horrible', 'atrocious', 'hypocrisy', 'irony']

def rate_from_tweet(tweet, positives, negatives):
	"""The tweet parameter is a string that represents a tweet. 
	The positives parameter is a list of strings that indicate a
	positive review of the moview. The negatives parameter is 
	similar to the positives parameter except it contains words
	with a negative review of whatever it is reviewing."""
	temp = tweet 
	tweet_words = re.sub("[^\w]", " ",  temp).split()
	not_flag = False
	total = 0
	for word in tweet_words:
		if word == 'not':
			not_flag = True
		elif word in positives:
			if not_flag:
				total -= 1
				not_flag = False
			else:
				total += 1
		elif word in negatives:
			if not_flag:
				total += 1
				not_flag = False
			else:
				total -= 1

	return total

def most_controversial_award(relationships, positives, negatives):
	"""Takes in the relationships between a tweetStringID and an award 
	in the form of a dictionary. Also takes in the list of tweets. 

	Part of the process calls for a dictionary 'ratings' where the key 
	is the award and the value is the cumulation of returned totals returned
	from rate_from_tweet for tweets related to that award. 

	Returns: Prints both the most agreeable and most controversial awards 
	based on a rating given from rate_from_tweet function."""
	ratings = {}
	for relationship in relationships:
		for tweet in relationships[relationship]:
			if relationship in ratings:
				ratings[relationship] += rate_from_tweet(tweet, positives, negatives)
			else:
				ratings[relationship] = rate_from_tweet(tweet, positives, negatives)

	agreeable = max(ratings.values())
	controversial = min(ratings.values())	

	print "The most agreed upon award(s): " + ', '.join(str(e) for e in [key for key, value in ratings.items() if value == agreeable])
	print "The most controversial award(s): " + ', '.join(str(e) for e in [key for key, value in ratings.items() if value == controversial])

def sentiment():
	tweets = gt.read_tweets_with_metadata('goldenglobes.tab')
	with open('categories.json') as categories_file:
	    categories = json.load(categories_file)
	most_controversial_award(rel.get_award_relationships(tweets, categories), positives, negatives)

