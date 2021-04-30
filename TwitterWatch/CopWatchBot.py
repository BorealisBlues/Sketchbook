## CopWatchBot.py

import discord
from discord.ext import commands
import json
from twython import TwythonStreamer

from dotenv import load_dotenv

## Environment Variables read from a .env file in the working directory
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
TWITTER_KEY = os.getenv('TWITTER_KEY')
TWITTER_SECRET = os.getenv('TWITTER_SECRET')

## get Oauth from twitter
twitter = Twython(TWITTER_KEY,TWITTER_SECRET)

## Version variable
version = '0.1'

## to set command prefix and shorten future code
bot = commands.Bot(command_prefx='%')

## logCommand logs the command and author to the console
def logCommand(ctx):
    print (f'{ctx.author} has issued the {ctx.command} command!')


## Create a class that inherits TwythonStreamer
class TweetStreamer(TwythonStreamer):

##  Recieved Data
    def on_success(self,data):
        
##      collects data in english
        if (data['lang'] == 'en'):
            tweet_text = tweet['text']
            
##  if there is a problem with the API
    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()

## on_ready events trigger on bot connect
@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
            f'{bot.user.name} is connected to the following guild: \n'
            f'{guild.name}(id: {guild.id})'
          )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

## the %version command replies with the current version
@bot.command(name='version', help='replies with current version')
async def getVersion(ctx):
    logCommand(ctx)
    await ctx.send(f'my current version is: {version}, thank you for asking! :relaxed:')
