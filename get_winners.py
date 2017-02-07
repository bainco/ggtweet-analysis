import globes_tweets as gt
import get_award_relationships as ga
import name_proc as np
import json
import operator
# from twitter_connect import *

def getTweetsByCategory(tweets):
    with open('categories.json') as categories_file:
        categories = json.load(categories_file)
    return ga.get_award_relationships(tweets, categories)

def findWinners(tweetsByCat):
    awards = {}
    for key in tweetsByCat:
        # print "AWARD: ", key
        potential_dict = {}
        curr_award_tweets = tweetsByCat[key]
        for tweet in curr_award_tweets:
            names = np.get_names(tweet)
            for name in names:
                if name in potential_dict:
                    potential_dict[name] += 1
                else:
                    potential_dict[name] = 1
        # print potential_dict
        award_winner = max(potential_dict.iteritems(), key = operator.itemgetter(1))[0]
        # if award_winner[0] == '@':
        #     award_winner_name = lookup_handle(award_winner)
        # else:
        #     award_winner_name = award_winner
        print "AWARD: ", key, ", WINNER:", award_winner
        awards[key] = award_winner
    return awards


if __name__ == "__main__":
    tweetsByCat = getTweetsByCategory()
    a = findWinners(tweetsByCat)
