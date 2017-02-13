import re
from globes_tweets import *


tweets = read_tweets_with_metadata('globestweets.txt')
awardsRegEx = r"Best(?=\s[A-Z])(\s([A-Z]\w+|in|an|a|for|or|-))+"

stop = ['TV', 'Musical or Comedy', 'Role', 'Limited', 'Film']
accept = ['Drama', 'Musical', 'Picture', 'Director', 'Screenplay', 'Song', 'Score', 'Film', 'Series', 'Television']
tags = ['Drama', 'Comedy', 'Musical']
categories = set()


for tweet in tweets:
    test = re.search(awardsRegEx, tweet['text'])
    if test and test.group(0).rsplit(None, 1)[-1] in accept:
        wordInStop = False
        for word in stop:
            if word in test.group(0):
                wordInStop = True
                break
        subsetOfAdded = False
        for cat in categories:
            if test.group(0) in cat:
                subsetOfAdded = True
                break
        tagAndDash = True
        for word in tags:
            if word in test.group(0):
                tagAndDash = False
                if '-' in test.group(0):
                    tagAndDash = True
                break
        if not wordInStop:
            if not subsetOfAdded:
                if tagAndDash:
                    categories.add(test.group(0))

for category in categories:
    print category

print "LEN CAT:", str(len(categories))
