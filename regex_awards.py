import re
from globes_tweets import *


tweets = read_tweets_with_metadata('globestweets.txt')
awardsRegEx = r"Best(?=\s[A-Z])(\s([A-Z]\w+|in|an|a|for|or|-))+"

# stop = ['and', 'a', 'in', '-', 'for']
accept = ['Drama', 'Musical', 'Picture', 'Director', 'Screenplay', 'Score', 'Song', 'Film', 'Series', 'Television']

categories = set()


for tweet in tweets:
    test = re.search(awardsRegEx, tweet['text'])
    if test and test.group(0).rsplit(None, 1)[-1] in accept:
        categories.add(test.group(0))

for category in categories:
    print category
