import csv, sys, nltk
from globes_tweets import read_tweets_with_metadata
from nltk.tag import pos_tag
from nltk.tree import Tree
from nltk.chunk import ne_chunk
from nltk.tokenize import TweetTokenizer
from itertools import chain
#import imdb

# Adapted from get_first_person.py from IMDbPY
# Not currently used
def lookup_name(aName):
    i = imdb.IMDb()

    in_encoding = sys.stdin.encoding or sys.getdefaultencoding()
    out_encoding = sys.stdout.encoding or sys.getdefaultencoding()

    name = unicode(aName, in_encoding, 'replace')
    try:
        # Do the search, and get the results (a list of Person objects).
        results = i.search_person(aName)

    except imdb.IMDbError, e:
        print "Probably you're not connected to Internet.  Complete error report:"
        print e
        sys.exit(3)

    if not results:
        print 'No matches for "%s", sorry.' % aName.encode(out_encoding, 'replace')
        sys.exit(0)

    # Print only the first result.
    print '    Best match for "%s"' % aName.encode(out_encoding, 'replace')

    # This is a Person instance.
    person = results[0]

    print person
    # So far the Person object only contains basic information like the
    # name; retrieve main information:

    # THIS METHOD GETS EXTRA STUFF. What movie? Years, etc.

    #i.update(person)

    #print person.summary().encode(out_encoding, 'replace')

def get_names(aTweet):
    """

    returns: list of dictionaries where each dictionary has key 'name'
    """

    ## TODO: In the future, I'd like this to also tag possible roles in
    #  movies (e.g. screen writer, director, etc.)

    tokens = tokenize(aTweet)
    taggedTokens = pos_tag(tokens)

    PNchunks = [chunk for chunk in ne_chunk(taggedTokens) if isinstance(chunk, Tree)]

    possible_names = [ " ".join(pair) for pair in nltk.bigrams([i[0] for i in list(chain(*[chunk.leaves() for chunk in PNchunks]))])]

    return possible_names


def tokenize(aTweet):
    """ Method to pass a sentence to NLTK and tokenize it.
        returns: a list of words in the input sentence
    """
    tknzr = TweetTokenizer()
    tokens = tknzr.tokenize(aTweet)
    return tokens

if __name__ == "__main__":
    #do the thing
    tweets = read_tweets_with_metadata('goldenglobes.tab')

    # REQUIRES NLTK with AVERAGED PERCEPTRON TAGGER, Tokenizer, and a couple
    # other NLTK downloads. Basically, if you get an NLTK error, just open up
    # a python console, and run nltk.download() and download the things it's mad
    # at you for.

    # EXAMPLE:
    aTweet = tweets[0]['text']
    print get_names(aTweet)
