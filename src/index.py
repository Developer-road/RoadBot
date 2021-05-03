import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re

bot = commands.Bot(command_prefix='-', description="This is a Helper Bot")

@bot.command()
async def pin(ctx):
    await ctx.send(':thumbsup: ')

@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.command()
async def hi(ctx):
    await ctx.send('Hello, How are you? I hope well')

@bot.command()
async def fine(ctx):
    await ctx.send('MMM I dont understand what is fine')


@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Developer Road is a platform for programmers made by programmers, we focus on sharing knowledge about any technology field. If you like to share knowledge and learn from awesome people with similar interests Developer Road is a superb choice.", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/834455100822650880/838796689841061918/1.png?width=473&height=473")

    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    print(search_results)
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Developer Road", url="http://www.twitch.tv/developerroad"))
    print('My Ready is Body')




bot.run("TOP SECRET")

