import re

positives = ['good', 'nice', 'terrific', 'great', 'amazing', 'proud']
negatives = ['bad', 'terrible', 'horrific', 'horrible', 'atrocious', 'hypocrisy', 'irony']

def rate_from_tweet(tweet, positives, negatives):
	'''The tweet parameter is a string that represents a tweet. 
	The positives parameter is a list of strings that indicate a
	positive review of the moview. The negatives parameter is 
	similar to the positives parameter except it contains words
	with a negative review of whatever it is reviewing.'''
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

	if total == 0:
		return 'neutral'
	elif total > 0: 
		return '+'
	elif total < 0:
		return '-'


# Test 1: Does rate_from_tweet properly parse words, while omitting 
# 		  spaces and punctuation?
## rate_from_tweet("Hi. My name is Austin Kim!",[],[])
## should return ['Hi', 'My', 'name', 'is', 'Austin', 'Kim']