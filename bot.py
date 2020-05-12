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
        newNick = random_word()
        await ctx.channel.send('I bestow upon you the name of ༼ つ ◕◡◕ ༽つ **{0}**'.format(newNick.capitalize()))

        topExampleUrl = 'https://api.wordnik.com/v4/word.json/{0}/topExample?useCanonical=false&api_key={1}'.format(newNick, api_token)
        req = urllib.request.Request(topExampleUrl)
        response = urllib.request.urlopen(req)
        data = response.read()
        values = json.loads(data)
        text = values["text"]

        splitStr = text.split(newNick)

        await ctx.channel.send('{0}**{1}**{2}'.format(splitStr[0], newNick,splitStr[1]))
        await member.edit(nick=newNick.capitalize())

    except Exception as e:
                print(e)

@bot.command(case_insensitive=True)
async def definition(ctx):

    try:
        member = ctx.author
        nickname = member.nick

        definitionUrl = 'https://api.wordnik.com/v4/word.json/{0}/definitions?limit=1&includeRelated=false&sourceDictionaries=wordnet&useCanonical=false&includeTags=false&api_key={1}'.format(nickname.lower(), api_token)
        req = urllib.request.Request(definitionUrl)
        response = urllib.request.urlopen(req)
        data = response.read()
        values = json.loads(data)
        text = values[0]["text"]

        await ctx.channel.send('**{0}** - {1}'.format(nickname, text))

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
    
    
