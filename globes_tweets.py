import sys

def read_tweets(fname):
    tweets = []
    tweets_file = open(fname, 'rb')

    for line in tweets_file:
        tweets.append(line[1:len(line) - 2])

    print str(tweets[0:10])
    return tweets



read_tweets('globestweets.txt')
