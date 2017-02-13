import globes_tweets as gt
import get_award_relationships as ga
import name_proc as np
import json
import operator
import get_presenters as gp
import get_hosts as gh
import get_winners as gw
import reviews as rev



if __name__ == "__main__":
  np.initialize_names()
  tweets = gt.read_tweets_with_metadata('goldenglobes.tab')

  #get hosts
  host = gh.findHosts(tweets)
  print "HOST:", host, "\n"

  #get winners
  print 'AWARD WINNERS'
  tweets_by_cat = gw.getTweetsByCategory(tweets)
  award_winners = gw.findWinners(tweets_by_cat)
  #print "WINNERS:", str(award_winners)
  print "\n"

  #get presenters
  print "PRESENTERS"
  winners_list = award_winners.values()
  winners_list.append('GoldenGlobes')
  winners_list.append('Golden Globe Awards')
  winners_list.append('Golden Globe')
  categories_to_presenters = gp.get_presenters(tweets_by_cat, winners_list)
  for category in categories_to_presenters:
    print 'AWARD:', category, ', PRESENTERS:', ', '.join(categories_to_presenters[category])
  print "\n"

  #sentiment analysis
  rev.sentiment()
