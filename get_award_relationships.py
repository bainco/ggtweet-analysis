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
    Returns: dictionary of award to a list of tweets
    """
    award_relationships = {}
    for tweet in tweets:
        if  get_award_relationship(tweet, categories) != None:
            ret_category = get_award_relationship(tweet, categories)
            if ret_category in award_relationships:
                award_relationships[ret_category].append(tweet['text'])
            else:
                award_relationships[ret_category] = [tweet['text']]
    return award_relationships

if __name__ == "__main__":
    tweets = gt.read_tweets_with_metadata('goldenglobes.tab')
    with open('categories.json') as categories_file:
        categories = json.load(categories_file)
    print get_award_relationships(tweets, categories)
