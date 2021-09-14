import tweepy
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

## TESTING VARIABLES

wordlist = ['test', 'police']



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

def GetUserID(user):
    userobj = api.get_user(user)
    print(f'the user {user} corresponds to username: {userobj.name}')
    print(f'the user {user} corresponds to user ID: {userobj.id}')
    return userobj.id, userobj.name

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
        #print(f'{tweet.user.name} said {tweet.text}')
        if CheckKeyWords(wordlist, tweet.text):
            print(f'MATCH FOUND {tweet.user.name}:{tweet.text}')
        else:
            print(f'NO MATCH {tweet.user.name}:{tweet.text}')

def StartStream(userid):
    ## steaming tester
    class MyStreamListener(tweepy.StreamListener):
        def __init__(self, api):
            self.api = api
            self.me = api.me()

        def on_status(self, tweet): #runs when a tweet matching the filter is detected
            if CheckKeyWords(wordlist, tweet.text):
                print(f'MATCH FOUND {tweet.user.name}:{tweet.text}')
            else:
                print(f'NO MATCH {tweet.user.name}:{tweet.text}')

        def on_error(self, status):
            print ("error detected", status)
    tweets_listener = MyStreamListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(follow=[str(userid)], is_async=True)

def CheckKeyWords(wordlist, tweet):
    for word in wordlist:
        if word.lower() in tweet.lower():
            return True
        else:
            return False
        
api = Authorize()
userid, username = GetUserID('scanthepolice')
GetUserTimeline(userid)
StartStream(userid)
