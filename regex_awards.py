import re
from globes_tweets import *



tweets = read_tweets_with_metadata('goldenglobes.tab')
awardsRegEx = r"Best(?=\s[A-Z])(\s([A-Z]\w+|in a|an|for|or|-))+"

stop = ['TV', 'Musical or Comedy', 'Role', 'Limited', 'Film']
accept = ['Drama', 'Musical', 'Picture', 'Director', 'Screenplay', 'Song', 'Score', 'Film', 'Series', 'Television']
tags = ['Drama', 'Comedy', 'Musical']
ending_words = ['Song', 'Director', 'Screenplay', 'Score']

categories = set()
cat_dict = {}


for tweet in tweets:
    test = re.search(awardsRegEx, tweet['text'])
    print
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
        valid_end = True
        for word in ending_words:
            if word in test.group(0):
                valid_end = False
                if word == test.group(0).rsplit(None, 1)[-1]:
                    valid_end = True
        valid_pic = True
        if "Picture" in test.group(0):
            valid_pic = False
            if "Motion" in test.group(0):
                valid_pic = True

        if not wordInStop:
            if valid_end:
                if valid_pic:
                    if "Original" not in test.group(0):
                        if test.group(0) in cat_dict.keys():
                            cat_dict[test.group(0)] = cat_dict[test.group(0)] + 1
                        else:
                            cat_dict[test.group(0)] = 1
                        if not subsetOfAdded:
                            if tagAndDash:
                                categories.add(test.group(0))


print "CAT DICT:", str(cat_dict)
i = 0
for category in categories:
    if cat_dict[category] > 15:
        print category
        i+= 1


print "LEN CAT:", str(i)
