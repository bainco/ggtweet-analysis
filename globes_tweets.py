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

def read_md_tweets_with_train(fname):

    f = open(fname, 'r')
    f_lines = f.readlines()
    tweets = []
    for line in f_lines:
        tweets.append(line.split('||'))


    print "Done reading tweets"

    return tweets

def train_fact_alt(tweets):
    hope = {}
    fact = {}
    unrelated = {}

    for tweet in tweets:
        status = int(tweet[0])
        t_tokens = tokenize(tweet[1])
        if status == -2:
            unrelated = addTokensToDict(unrelated, t_tokens)
        elif status == -1:
            hope = addTokensToDict(hope, t_tokens)
        elif status == 1:
            fact = addTokensToDict(fact, t_tokens)

    return [unrelated, hope, fact]

def addTokensToDict(d, t_tokens):
    for t in t_tokens:
        #print t
        if t == u'\u201d':
            return d
        t = str(t).lower()
        print "T:" + t + ", ord:" + str(ord(t[0]))
        if t in d:
            d[t]+= 1
        else:
            d[t] = 1

    return d

def classifyTweet(tweet, unrelated, hope, fact):
    tokens = tokenize(tweet)
    hope_sum = 0
    unrelated_sum = 0
    fact_sum = 0
    for t in tokens:
        hope_sum+= getTokenValInDict(t, hope)
        unrelated_sum+= getTokenValInDict(t, unrelated)
        fact_sum+= getTokenValInDict(t, fact)

    sum_list = [hope_sum, fact_sum]
    m_ind = sum_list.index(max(sum_list))
    if m_ind == 0:
        return "hope"
    else:
        return "fact"



def getTokenValInDict(token, dict):
    if token == u'\u201d':
        return 0
    token = str(token).lower()
    if token in dict:
        return dict[token]
    else:
        return 0

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
    # print "BEFORE, " + a_tweet
    a_tweet = a_tweet.replace('"', '').strip()
    # print "AFTER, " + a_tweet
    tknzr = TweetTokenizer()

    tokens = tknzr.tokenize(a_tweet)
    # print str(tokens)
    return tokens

tweets = read_md_tweets_with_train('globestweets.txt')
res = train_fact_alt(tweets)
dec = classifyTweet('"RT @goldenglobes: Congratulations to Damien Chazelle - Best Screenplay - La La Land (@LaLaLand) - #GoldenGlobes"', res[0], res[1], res[2])
print str(dec)
