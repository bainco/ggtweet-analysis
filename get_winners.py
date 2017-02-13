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
        # print "POT:", potential_dict
        award_winner = max(potential_dict.iteritems(), key = operator.itemgetter(1))[0]
        # if award_winner[0] == '@':
        #     award_winner_name = lookup_handle(award_winner)
        # elif award_winner[0] == '#':
        #     award_winner_name = award_winner[1:]
        # else:
        #     award_winner_name = award_winner
        print "AWARD: ", key
        print "        WINNER:", award_winner
        awards[key] = award_winner
        winner_lower = award_winner.lower().replace(" ", "")
        # print "award_lower:", winner_lower
        del potential_dict[award_winner]
        nominees = []
        # print str(potential_dict)
        while len(nominees) != 4:
            len_dict = len(potential_dict)
            if len_dict == 0:
                break
            nom_key =  max(potential_dict.iteritems(), key = operator.itemgetter(1))[0]
            nom_key = str(nom_key)
            # print "NOM_KEY:", nom_key
            if ((nom_key[0] != '#')
                and (nom_key[0] != '@')
                and ("golden" not in nom_key.lower())
                and ("globes" not in nom_key.lower())
                and (winner_lower not in nom_key.lower().replace(" ", ""))):
                nominees.append(nom_key)
            del potential_dict[nom_key]

        print "        nominees:", str(nominees)

    return awards


if __name__ == "__main__":
    np.initialize_names()
    tweets = gt.read_tweets_with_metadata('goldenglobes.tab')
    tweetsByCat = getTweetsByCategory(tweets)
    a = findWinners(tweetsByCat)
