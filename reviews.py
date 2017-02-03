import re
import globes_tweets as gt
import json

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

def most_controversial_award(relationships, tweets, positives, negatives, flag):
	"""Takes in the relationships between a tweetStringID and an award 
	in the form of a dictionary. Also takes in the list of tweets. 

	Part of the process calls for a dictionary 'ratings' where the key 
	is the award and the value is the cumulation of returned totals returned
	from rate_from_tweet for tweets related to that award. 

	Returns: a list of most controversial(flag = true) or agreed (flag = false) awards (key with the lowest value)"""
	ratings = {}
	for relationship in relationships:
		for tweet in tweets:
			if tweet['tweetIDString'] == relationship:
				if relationships[relationship] in ratings:
					ratings[relationships[relationship]] += rate_from_tweet(tweet['text'], positives, negatives)
				else:
					ratings[relationships[relationship]] = rate_from_tweet(tweet['text'], positives, negatives)

	controversial = []

	if flag:
		value = 1000000
		for rating in ratings: 
			if ratings[rating] == value: 
				controversial.append(rating)
			if ratings[rating] < value:
				controversial = []
				controversial.append(rating)
				value = ratings[rating]
	else:
		value = -1000000
		for rating in ratings: 
			if ratings[rating] == value: 
				controversial.append(rating)
			if ratings[rating] > value:
				controversial = []
				controversial.append(rating)
				value = ratings[rating]

	return controversial

def main():
    """
    function for example usage; not code for actual project (would need to parameterize)
    """
    tweets = gt.read_tweets_with_metadata('goldenglobes.tab')
    with open('categories.json') as categories_file:
        categories = json.load(categories_file)
    return most_controversial_award(get_award_relationships(tweets, categories), tweets, positives, negatives, False)

