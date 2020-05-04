import os
import json
import asyncio
import urllib
from discord.ext import commands

bot = commands.Bot(command_prefix='gib ')

api_token = os.environ['API_TOKEN']

url = 'http://api.wordnik.com:80/v4/words.json/randomWords?hasDictionaryDef=true&minCorpusCount=0&minLength=5&maxLength=15&limit=1&api_key={0}'.format(api_token)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def exit(ctx):
    await bot.logout()

@bot.command()
async def name(ctx):
        member = ctx.author
        newNick = random_word().capitalize()
        await ctx.channel.send('I bestow upon you the name of ༼ つ ◕_◕ ༽つ {0}'.format(newNick))
        await member.edit(nick=newNick)

def random_word():
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    data = response.read()
    values = json.loads(data)
    word = values[0]["word"]
    return(word)

if __name__ == "__main__":
    token = os.environ['CLIENT_TOKEN']
    bot.run(token)
    
    