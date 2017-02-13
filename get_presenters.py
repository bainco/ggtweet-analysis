import globes_tweets as gt
import get_award_relationships as ga
import name_proc as np
import json
import twitter_connect as tc

def get_presenters(award_to_tweets, exclude = []):
    categories_to_presenters = {}
    np.initialize_names()
    for category in award_to_tweets:
        categories_to_presenters[category] = get_presenters_of_category(award_to_tweets[category], exclude)
    return categories_to_presenters

def get_presenters_of_category(tweets, exclude):
    presenters = []
    presenter_totals = {}
    presenter_keywords = ['presents', 'present', 'presenting', 'introduce', 'introduces', 'introducing', 'presenters', 'presenter', 'presented']
    for tweet in tweets:
        if any(keyword in tweet for keyword in presenter_keywords):
            # Probalby also check to see if this person isn't the winner
            for name in np.get_names(tweet):
                translated_name = name
                if name[0] == '@':
                    translated_name = tc.lookup_handle(name)
                elif name[0] == '#':
                    translated_name = name[1:]
                if translated_name in presenter_totals.keys() and translated_name not in exclude:
                    presenter_totals[translated_name] += 1
                elif translated_name not in exclude:
                    presenter_totals[translated_name] = 1
    for p in presenter_totals:
        if presenter_totals[p] > 1: # TODO placeholder value
            presenters.append(p)
    return presenters

if __name__ == "__main__":
    tweets = gt.read_tweets_with_metadata('goldenglobes.tab')
    with open('categories.json') as categories_file:
        categories = json.load(categories_file)
    categories_to_presenters = get_presenters(ga.get_award_relationships(tweets, categories))
    for category in categories_to_presenters:
        print 'AWARD:', category, ', PRESENTERS:', ', '.join(categories_to_presenters[category])
