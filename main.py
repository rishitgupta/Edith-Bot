# add on_delete_message()

import discord
from discord.ext import commands
from discord.utils import get

import random
import io, aiohttp

from googlesearch import search
import youtube_dl

import urbandictionary as ud

client = commands.Bot(command_prefix = "", case_insensitive = True)

media = {
    # Friends
    "nooo": [r"https://media1.tenor.com/images/3e9e0a976d582002a4a02d690fbc12f9/tenor.gif"],
    "bhap": [r"https://media1.tenor.com/images/a69b9e8e2990a74f0fdfe067c0f47b67/tenor.gif"],
    "thumbsup": [r"https://media1.tenor.com/images/038e36f6bd6374e12084feb841a8d51f/tenor.gif"],
    "shocked": [r"https://media1.tenor.com/images/a5a7cc8535b02e60462214be2f5a3a67/tenor.gif"],
    "wisdomous": [r"https://media1.tenor.com/images/883d3cdb1d0d95b19d4f8b0411941143/tenor.gif"],
    "middle-finger": [r"https://media.tenor.com/images/b92364f634c5375c1d1cb5d0ea0d4979/tenor.gif"],
    # Brooklyn Nine-Nine
    "noice": [r"https://media.tenor.com/images/098e4852dfdc41991add5983e9262a92/tenor.gif"],
    "cool": [r"https://i.pinimg.com/originals/4f/db/37/4fdb373ebe3e8cec0f6ad5a4345ad011.gif"],
    "toit": [r"https://basicallylaurenslifetravel.files.wordpress.com/2019/04/tumblr_p0gl7i7p5i1qjvfkco2_500.gif"],
    # How I Met Your Mother
    "woo": [r"https://media1.tenor.com/images/b15404e06ff41a0cbed2153398b1a8ab/tenor.gif"],
    "kill": [r"https://media1.tenor.com/images/61ae345e267e9ce138708d8058996bf4/tenor.gif"],
    # Memes
    "maybe": [r"https://media.tenor.com/images/6bdd650af717980d5d898d4fd0b8ad52/tenor.gif"],
    "nikal": [r"https://media.tenor.com/images/7e6a7b73faa414e321811e0ecb34519e/tenor.gif"],
    # Misc
    "excellent": [r"https://media1.tenor.com/images/9e3409f358c9cec06061c1ec76d86d47/tenor.gif?itemid=4076853"],
}

@client.event
async def on_ready():
    print("-"*10)
    print("Bot loading...")
    print()
    # Configuring GIFs
    for i in media:
        async with aiohttp.ClientSession() as session:
            async with session.get(media[i][0]) as resp:
                if not resp.status == 200: # HTTP response status code 200 means okay
                    print(f"Could not download file: {i}")
                    continue
                media[i].append(io.BytesIO(await resp.read()))
                print(f"\"{i}\" loaded", end="; ")
    print("\n")
    print("All systems, good to go.")
    print("-"*10)

# Ping
@client.command(aliases=["whatistheping", "whatstheping", "wotisleping"])
async def ping(ctx):
    await ctx.send(f"Pong! The ping is {round(client.latency * 1000)}ms.")

# Magic 8-Ball
@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
    responses = ["_Sure, honey, sure._", "You really need to ask?", "Of course, bruv.", "Bhai mai bhagwaan nahi hoon", "DUH.", "Never in a million years", "Koi chance hi nahi hai boss", "_Mayyyyybeeeee_", "Definitely", "Why even-", "Ghanta."]
    await ctx.send(random.choice(responses))

# Clear
@client.command()
async def clear(ctx, amount=0):
    await ctx.channel.purge(limit=amount)

# Chandler
@client.command()
async def chandler(ctx, name, *, adj):
    if name == "more" or name == "less" or adj == "more" or adj == "less":
        pass
    else:
        await ctx.channel.purge(limit=1)
        await ctx.send(f"Could {name} BE any {adj}?")

# Introduction
@client.command(aliases=["whatisedith, whatsedith, introduction"])
async def edith(ctx):
    await ctx.send("> Heyo, this is Edith. \n> A bot designed to mess around with you. \n> Bask in the sheer suffering that I shall wreak upon your puny existences, \n> And a little bit of fun, too. :)")

@client.command(aliases=["googlesearch"])
async def google(ctx, *, query):
    for j in search(query, lang="en", safe="off", num=3, stop=3, pause=2, verify_ssl=True):
        await ctx.send(j)

# <-----------SONGS-------------->
@client.command(aliases=["joinedith"])
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@client.command(aliases=["leaveedith"])
async def leave(ctx):
    await ctx.voice_client.disconnect()

@client.command(aliases=["yt", "song", "music", "bajaa"])
async def youtube(ctx, *, song_name):
    for j in search(f"{song_name} song YouTube", lang="en", safe="off", num=1, stop=1, pause=2, verify_ssl=True):
        song_link = j

@client.command(aliases=["urbandict", "define", "ud"])
async def urbandictionary(ctx, *, term):
    definitions = ud.define(term)
    await ctx.send(f"> **_{term.title()}_**")
    for i in range(0, 3):
        tempDef = definitions[i].definition.replace("[", "").replace("]", "").replace("\n", "\n> \t")
        tempEx = definitions[i].example.replace("[", "").replace("]", "").replace("\n", "\n> \t")
        await ctx.send(f"> **{i+1}.** \n> \t{tempDef} \n> \t_\"{tempEx}\"_")

# <-------------GIFS------------->
@client.command(aliases=["listofgifs", "gif-list"])
async def gifList(ctx):
    list_of_gifs = ""
    for i in media:
        list_of_gifs += "\n"
        list_of_gifs += f"> _{i}_"
    await ctx.send(f"This is a list of all the GIFs an extrordinary bot like yours truly has to offer: {list_of_gifs}")
# Friends
@client.command(aliases=["noooo", "nooooo"])
async def nooo(ctx):
    await ctx.send(file=discord.File(media["nooo"][1], "nooo.gif"))
@client.command()
async def  bhap(ctx):
    await ctx.send(file=discord.File(media["bhap"][1], "bhap.gif"))
@client.command(aliases=["goodjob", "greatjob", "badiya"])
async def thumbsup(ctx):
    await ctx.send(file=discord.File(media["thumbsup"][1], "thumbsup.gif"))
@client.command(aliases=["gasp"])
async def shocked(ctx):
    await ctx.send(file=discord.File(media["shocked"][1], "shocked.gif"))
@client.command(aliases=["wise", "wisdom", "smart"])
async def wisdomous(ctx):
    await ctx.send(file=discord.File(media["wisdomous"][1], "wisdomous.gif"))
@client.command(aliases=["middle-finger", ":middle_finger:"])
async def middleFinger(ctx):
    await ctx.send(file=discord.File(media["middle-finger"][1], "middle-finger.gif"))
# Brooklyn Nine-Nine
@client.command(aliases=["nice"])
async def noice(ctx):
    await ctx.send(file=discord.File(media["noice"][1], "noice.gif"))
@client.command(aliases=["coolcoolcool"])
async def cool(ctx):
    await ctx.send(file=discord.File(media["cool"][1], "cool.gif"))
@client.command()
async def toit(ctx):
    await ctx.send(file=discord.File(media["toit"][1], "toit.gif"))
# How I Met Your Mother
@client.command()
async def woo(ctx):
    await ctx.send(file=discord.File(media["woo"][1], "woo.gif"))
@client.command(aliases=["killme", "killmenow", "kmn"])
async def kill(ctx):
    await ctx.send(file=discord.File(media["kill"][1], "kill.gif"))
# Memes
@client.command(aliases=["maybeee", "mayyybeee"])
async def mayyybe(ctx):
    await ctx.send(file=discord.File(media["maybe"][1], "maybe.gif"))
@client.command(aliases=["nikallawde", "nikallavde", "pehlifursatmeinnikal"])
async def nikal(ctx):
    await ctx.send(file=discord.File(media["nikal"][1], "nikal.gif"))
# Misc.
@client.command(aliases=["ahhhhh"])
async def excellent(ctx):
    await ctx.send(file=discord.File(media["excellent"][1], "excellent.gif"))

