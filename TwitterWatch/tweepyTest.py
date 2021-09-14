import tweepy
import json
import os
from dotenv import load_dotenv


## TO DO
## ADD IN DISCORD FRAMEWORK
## STORE LAST ~20~ TWEETS IN A LIST TO BE CHECKED AGAINST FOR KEYWORDS
## MAKE ACCESSIBLE
## ADD IN SIGNAL FRAMEWORK
## USER SETTABLE TWITTER USERS TO FOLLOW AND TRIGGER WORDS

## Environment Variables

load_dotenv()
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_KEY = os.getenv('ACCESS_KEY')
ACCESS_SECRET = os.getenv('ACCESS_TOKEN_SECRET')


def Authorize():
    ## Authenticators
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    ## Create API Object
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

def TestTweet():
    ## Create a tweet
    api.update_status('tweepy Test')

def GetOwnTimeline():
    ## timeline retrieval
    timeline = api.home_timeline()
    for tweet in timeline:
        print(f'{tweet.user.name} said {tweet.text}') # calls the last 20 tweets

def GetUserTimeline(user):
    ## Retrieves timeline of another user
    user = api.get_user(user)
    print('User details:')
    print(user.name)
    print(user.description)
    print(user.location)
    print('\n')

    print('last 20 tweets:')
    for tweet in user.timeline():
        print(f'{tweet.user.name} said {tweet.text}')

def StartStream():
    ## steaming tester
    class MyStreamListener(tweepy.StreamListener):
        def __init__(self, api):
            self.api = api
            self.me = api.me()

        def on_status(self, tweet): #runs when a tweet matching the filter is detected
            print(f'{tweet.user.name}:{tweet.text}')

        def on_error(self, status):
            print ("error detected", status)
    tweets_listener = MyStreamListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(follow=['1269039873488535555'], is_async=True)


api = Authorize()
GetUserTimeline('scanthepolice')
StartStream()
