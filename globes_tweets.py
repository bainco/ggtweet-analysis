import sys, csv, itertools
from nltk.tokenize import TweetTokenizer

# This might be useful:
# http://www.nltk.org/howto/twitter.html

def read_tweets_with_metadata(fname):
    """ Alternate method to read in the tweets with metadata text file. This
    also returns a list of tweets, but instead of just strings, they're
    dicts with some other stuff in them.

    returns: list of tweets
    """
    tweets = []

    with open(fname,'r') as f:
        reader1,reader2=itertools.tee(csv.reader(f,delimiter='\t'))
        del reader1
        for row in reader2:
            if len(row) == 5:
                theTweet = {"text": row[0], "tweeter": row[1], "userIDString":row[2], "tweetIDString":row[3], "timestamp":row[4]}
                tweets.append(theTweet)
            elif len(row) != 0:
                theTweet = {"text": row[0], "tweeter": '', "userIDString":'', "tweetIDString":'', "timestamp":''}
                tweets.append(theTweet)
    return tweets

def read_tweets(fname):

    tweets = []
    tweets_file = open(fname, 'rb')

    for line in tweets_file:
        tweets.append(line[1:len(line) - 2])

    #print str(tweets[0:10])
    #print len(tweets)

    tweets_file.close()

    return tweets

# TODO:
# At some point in here we need to extract links (cause that'll be annoying)
# Links are either retweets or photos right?

def tokenize(a_tweet):
    """ Method to pass a sentence to NLTK and tokenize it.
        returns: a list of words in the input sentence
    """
    tknzr = TweetTokenizer()

    tokens = tknzr.tokenize(a_tweet)
    return tokens

#tweets = read_tweets('globestweets.txt')
#print tokenize(tweets[0])
