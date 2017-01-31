import globes_tweets as gt
import json

def get_award_relationship(tweet, categories):
    """
    Takes in the tweets as dictionaries returned by read_tweets_with_metadata
    And categories as a list
    Returns: category if relationship exists, otherwise None
    """
    for category in categories:
        if category in tweet['text']:
            return category
    return None

def get_award_relationships(tweets, categories):
    """
    Takes in the tweets as dictionaries returned by read_tweets_with_metadata
    And categories as a list
    Returns: dictionary of tweetIDString to award
    """
    award_relationships = {}
    for tweet in tweets:
        if  get_award_relationship(tweet, categories) != None:
            award_relationships[tweet['tweetIDString']] = get_award_relationship(tweet, categories)
    return award_relationships


def main():
    """
    function for example usage; not code for actual project (would need to parameterize)
    currently returns dict of len 4202
    """
    tweets = gt.read_tweets_with_metadata('goldenglobes.tab')
    with open('nominees.json') as categories_file:
        categories = json.load(categories_file).keys()
    return get_award_relationships(tweets, categories)