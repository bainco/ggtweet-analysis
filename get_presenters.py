import globes_tweets as gt
import get_award_relationships as ga
import name_proc as np
import json

def get_presenters(award_to_tweets):
    categories_to_presenters = {}
    np.initialize_names()
    for category in award_to_tweets:
        categories_to_presenters[category] = get_presenters_of_category(award_to_tweets[category])
    return categories_to_presenters

def get_presenters_of_category(tweets):
    presenters = []
    presenter_totals = {}
    presenter_keywords = ['presents', 'present', 'presenting', 'introduce', 'introduces', 'introducing', 'presenters', 'presenter']
    for tweet in tweets:
        if any(keyword in tweet for keyword in presenter_keywords):
            for name in np.get_names(tweet):
                if name in presenter_totals.keys():
                    presenter_totals[name] += 1
                else:
                    presenter_totals[name] = 1
    for p in presenter_totals:
        if presenter_totals[p] > 5: # TODO placeholder value
            presenters.append(p)
    return presenters

def main():
    tweets = gt.read_tweets_with_metadata('goldenglobes.tab')
    with open('categories.json') as categories_file:
        categories = json.load(categories_file)
    return get_presenters(ga.get_award_relationships(tweets, categories))
