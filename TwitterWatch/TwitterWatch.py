import tweepy
import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

## TO DO
## ADD IN DISCORD FRAMEWORK
## MAKE ACCESSIBLE
## ADD IN SIGNAL FRAMEWORK
## USER SETTABLE TWITTER USERS TO FOLLOW AND SENTINEL WORDS
## RESTRUCTURE INSTANCE OF STEAMER TO HAVE CHECK KEYWORD FLAGS
    ## FOR USE IN PASSING *ALL* TWEETS MADE BY A USER

## ADDITIONAL ACCOUNTS TO CHECK -- WaywardStreamer // ChuckModi

## Environment Variables

load_dotenv()

## TWITTER ENV BLOCK
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_KEY = os.getenv('ACCESS_KEY')
ACCESS_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
CHANNEL_ID = os.getenv('CHANNEL_ID')


## DISCORD ENV BLOCK
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

## GLOBAL VARIABLES

wordList = ['test', 'police']
userList = ['scanthepolice']
version = '0.0.1'
enableLogging = True
isDebug = True


## ---------------------------
## TWITTER BLOCK OF FUNCTIONS
## ---------------------------
def Authorize():
    ## Authenticators
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    ## Create API Object
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

def GetUserID(user):
    userobj = api.get_user(user)
    print(f'the user {user} corresponds to username: {userobj.name}')
    print(f'the user {user} corresponds to user ID: {userobj.id}')
    return userobj.id

async def GetUserTimeline(user, ctx, doCheck):
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
        if CheckKeyWords(wordList, tweet.text):
            if enableLogging:
                print(f'MATCH FOUND {tweet.user.name}:{tweet.text}')
            await ctx.send(f'MATCH FOUND {tweet.user.name}:{tweet.text}')

        else:
            if enableLogging:
                print(f'NO MATCH {tweet.user.name}:{tweet.text}')
            if isDebug: #Only send non-matches if isDebug=True
                await ctx.send(f'NO MATCH {tweet.user.name}:{tweet.text}')


async def StartStream(userid, ctx, doCheck):
    ## steaming tester
    class MyStreamListener(tweepy.StreamListener):
        def __init__(self, api): #runs on initialization
            self.api = api
            self.me = api.me()

        async def on_status(self, tweet): #runs when a tweet matching the filter is detected
            if CheckKeyWords(wordlist, tweet.text):
                if enableLogging:
                    print(f'MATCH FOUND {tweet.user.name}:{tweet.text}')
                await ctx.send(f'MATCH FOUND {tweet.user.name}:{tweet.text}')
            else:
                if enableLogging:
                    print(f'NO MATCH {tweet.user.name}:{tweet.text}')
                if isDebug:
                    await ctx.send(f'NO MATCH {tweet.user.name}:{tweet.text}')

        def on_error(self, status): #runs when an error occurs
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


## ---------------------------
## DISCORD BLOCK OF FUNCTIONS
## ---------------------------

bot = commands.Bot(command_prefix='!')

def logCommand(ctx):
    #logCommand logs the command and author to the console IF enableLogging is True
    if enableLogging:
        print(f'{ctx.author} has issued the {ctx.command} command!')

@bot.event
async def on_ready():
    # on_ready prints the connected guilds and members on connection
    guild = discord.utils.get(bot.guilds)
    print(
            f'connected to the following guild: \n {guild.name}(id: {guild.id})'
          )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
    
@bot.command(name='version', help='replies with current version')
async def getVersion(ctx):
    ## the !version command replies with the current version
    logCommand(ctx)
    await ctx.send(f'my current version is: {version}, thank you for asking! :relaxed:')

@bot.command(name='SetKeywords', help='Sets Keywords to watch for')
async def setKeyWords(ctx, keywords):
    logCommand(ctx)
    wordList = keywords.split(',')
    await ctx.send(f'Current list of keywords is now {wordList}')

@bot.command(name='checkKeywords', help='replies with a list of current keywords')
async def getKeywords(ctx):
    logCommand(ctx)
    await ctx.send(f'Current list of keywords is {wordList}')
    
@bot.command(name='setUsers', help='sets a list of twitter users to check tweets of')
async def setUsers(ctx, users):
    logCommand(ctx)
    userList = keywords.split(',')
    await ctx.send(f'Current list of users is now {userList}')
    
@bot.command(name='getUsers', help='replies with a list of current users')
async def getUsers(ctx):
     logCommand(ctx)
     await ctx.send(f'Current list of users is {userList}')

@bot.command(name='startWatching', help='start watching a given user')
async def startWatching(ctx, user, doCheck=True):
    ## startWatching will initiate a stream for a given user
    try:
        userid = GetUserID(user)
    except Exception as e:
        print(f"an error has occoured! {e}")
        await ctx.send(f"an error has occoured! {e}")
    else:
        await GetUserTimeline(userid, ctx, doCheck)
        await StartStream(userid, ctx, doCheck)

@bot.command(name='setChannel', help='sets the channel to send updates to')
async def setChannel(ctx):
    #setChannel should set the global variable for the channel to send updates to
    updatesChannel=str(ctx.channel)
    
def main():
    
    ## TWITTER RUN BLOCK

    #userid = GetUserID('scanthepolice')
    #GetUserTimeline(userid)
    #StartStream(userid)
    
    ## DISCORD RUN BLOCK
    bot.run(TOKEN)
api = Authorize()
main()