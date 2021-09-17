## this is a suite of library functions to be used in the main file of tweepy test
## hopefully this makes things slightly neater
import discord
from discord.ext import commands

#sets the command prefix to !
bot = commands.Bot(command_prefix='!')


def logCommand(ctx):
    #logCommand logs the command and author to the console
    print(f'{ctx.author} has issued the {ctx.command} command!')


@bot.event
async def on_ready():
    # on_ready prints the connected guilds and members on connection
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
            f'{bot.user.name} is connected to the following guild: \n'
            f'{guild.name}(id: {guild.id})'
          )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')