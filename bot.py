import os
import json
import asyncio
import urllib
from discord.ext import commands

bot = commands.Bot(command_prefix='gib ', case_insensitive=True)

api_token = os.environ['API_TOKEN']

url = 'http://api.wordnik.com:80/v4/words.json/randomWords?hasDictionaryDef=true&minCorpusCount=0&minLength=5&maxLength=15&limit=1&api_key={0}'.format(api_token)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def exit(ctx):
    await bot.logout()

@bot.command(case_insensitive=True)
async def name(ctx):

    try:
        member = ctx.author
        newNick = random_word().capitalize()
        await ctx.channel.send('I bestow upon you the name of ༼ つ ◕_◕ ༽つ {0}'.format(newNick))
        await member.edit(nick=newNick)
    except Exception as e:
                print(e)

def random_word():
    try:
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        data = response.read()
        values = json.loads(data)
        word = values[0]["word"]
    except Exception as e:
                print(e)

    return(word)

if __name__ == "__main__":
    token = os.environ['CLIENT_TOKEN']
    try:
        bot.run(token)
    except Exception as e:
        print(e)
    
    
