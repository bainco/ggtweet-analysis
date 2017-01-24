import sys, csv
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
        reader=csv.reader(f,delimiter='\t')
        for text, tweeter, userIDString, tweetIDString, timestamp in reader:
            theTweet = {"text": text, "tweeter": tweeter, "userIDString":userIDString, "tweetIDString":tweetIDString, "timestamp":timestamp}
            tweets.append(theTweet)

    # Return reverse since the file was read in newest to oldest
    return tweets.reverse()

def read_tweets(fname):

    tweets = []
    tweets_file = open(fname, 'rb')

    for line in tweets_file:
        tweets.append(line[1:len(line) - 2])

    #print str(tweets[0:10])
    #print len(tweets)

    fname.close()

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
