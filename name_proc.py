import csv, sys, nltk
from globes_tweets import read_tweets_with_metadata
from nltk.tag import pos_tag
from nltk.tree import Tree
from nltk.chunk import ne_chunk
from nltk.tokenize import TweetTokenizer
from itertools import chain
import time
#import imdb

BABY_NAMES = []

def tokenize(aTweet):
    """ Method to pass a sentence to NLTK and tokenize it.
        returns: a list of words in the input sentence
    """
    tknzr = TweetTokenizer()
    tokens = tknzr.tokenize(aTweet)

    return tokens

def get_names(aTweet):
    print aTweet
    possible_names = set()
    tokens = tokenize(aTweet)
    for i in range(len(tokens) - 1):
        if (tokens[i] in BABY_NAMES) and tokens[i+1][0].isupper() and tokens[i+1].isalnum():
            possible_names.add((" ".join([tokens[i], tokens[i + 1]])))

    return possible_names


if __name__ == "__main__":
    #do the thing
    tweets = read_tweets_with_metadata('goldenglobes.tab')

    # Load in the baby names
    with open('yob2015.txt','r') as f:
        reader = csv.reader(f)
        for row in reader:
            BABY_NAMES.append(row[0])

    BABY_NAMES = BABY_NAMES[:1000]
    # EXAMPLE:
    for aTweet in tweets:
        if aTweet['text'][:2] != 'RT':
            print get_names(aTweet['text'])
