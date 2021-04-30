import tweepy
import json

from dotenv import load_dotenv


## Environment Variables
load_dotenv()
CONSUMER_KEY = os.getenv('twitter_consumer_key')
CONSUMER_SECRET = os.getenv('twitter_consumer_secret')
ACCESS_TOKEN = os.getenv('twitter_access_token')
ACCESS_TOKEN_SECRET = os.getenv('twitter_access_token_secret')

## Authenticators
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

## Create API Object
api = tweepy.API(auth, wait_on_rate_limit=True)

## Create a tweet
api.update_status('tweepy Test')

## timeline retrieval
timeline = api.home_timeline()
for tweet in timeline:
    print(f'{tweet.user.name} said {tweet.text}') # calls the last 20 tweets

## Retrieves timeline of another user
user = api.get_user('scanthepolice')
print('User details:')
print(user.name)
print(user.description)
print(user.location)

print('last 20 tweets:')
for tweet in user.timeline():
    print print(f'{tweet.user.name} said {tweet.text}')

## steaming tester
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet): #runs when a tweet matching the filter is detected
        print(f'{tweet.user.name}:{tweet.text}')

    def on_error(self, status):
        print ("error detected")
tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(follow=['scanthepolice'], languages=['en'])


    
