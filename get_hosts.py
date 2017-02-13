import globes_tweets as gt
import get_award_relationships as ga
import name_proc as np
import json
import operator
from twitter_connect import *

def findHosts(tweet, hosts_potential):
    host_keywords = ['host', 'hosts', 'hosting', 'monologue']
    if any(keyword in tweet for keyword in host_keywords):
        for name in np.get_names(tweet):
            if name in hosts_potential:
                hosts_potential[name] += 1
            else:
                hosts_potential[name] = 1
    return hosts_potential

def guess_host(hosts_potential):
    host_name = max(hosts_potential.iteritems(), key = operator.itemgetter(1))[0]

    if host_name[0] == '@':
        host_actual_name = lookup_handle(host_name)
    else:
        host_actual_name = host_name

    #print "HOST: ", host_actual_name
    return host_actual_name


if __name__ == "__main__":
    np.initialize_names()
    tweets = gt.read_tweets_with_metadata('goldenglobes.tab')
    #a = findHosts(tweets)
