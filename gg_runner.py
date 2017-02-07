import globes_tweets as gt
import get_award_relationships as ga
import name_proc as np
import json
import operator
import get_presenters as gp
import get_hosts as gh
import get_winners as gw



if __name__ == "__main__":
  np.initialize_names()
  tweets = gt.read_tweets_with_metadata('goldenglobes.tab')
  #get hosts
  host = gh.findHosts(tweets)
  print "HOST:", host
  #get winners
  tweets_by_cat = gw.getTweetsByCategory(tweets)
  award_winners = gw.findWinners(tweets_by_cat)
  #print "WINNERS:", str(award_winners)
