import globes_tweets as gt
import get_award_relationships as ga
import name_proc as np
import json
import operator
# from twitter_connect import *


def findHosts(tweets):
    hosts_potential = {}
    host_keywords = ['host', 'hosts', 'hosting', 'monologue']
    for t in tweets:
        tweet = t['text']
        if any(keyword in tweet for keyword in host_keywords):
            for name in np.get_names(tweet):
                if name in hosts_potential:
                    hosts_potential[name] += 1
                else:
                    hosts_potential[name] = 1

    print "HOSTS??: ", str(hosts_potential)
    host_name = max(hosts_potential.iteritems(), key = operator.itemgetter(1))[0]
    print "HOST: ", host_name
    return host_name

if __name__ == "__main__":
    np.initialize_names()
    tweets = gt.read_tweets_with_metadata('goldenglobes.tab')
    a = findHosts(tweets)