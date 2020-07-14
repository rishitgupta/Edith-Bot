# Excellent/Ah, Noice/Nice, Cool, Toit, Woooooo/Woohoo (Ted), nikal, knockknockknock, maybeeeeeee, nooo, haie (ross), damn

import discord
from discord.ext import commands

import random
import io, aiohttp

from googlesearch import search

client = commands.Bot(command_prefix = "")

media = {
    # Friends
    "nooo": [r"https://media1.tenor.com/images/3e9e0a976d582002a4a02d690fbc12f9/tenor.gif"],
    "bhap": [r"https://media1.tenor.com/images/a69b9e8e2990a74f0fdfe067c0f47b67/tenor.gif"],
    "middle-finger": [r"https://media.tenor.com/images/b92364f634c5375c1d1cb5d0ea0d4979/tenor.gif"],
    # Brooklyn Nine-Nine
    "noice": [r"https://media.tenor.com/images/098e4852dfdc41991add5983e9262a92/tenor.gif"],
    "cool": [r"https://i.pinimg.com/originals/4f/db/37/4fdb373ebe3e8cec0f6ad5a4345ad011.gif"],
    "toit": [r"https://basicallylaurenslifetravel.files.wordpress.com/2019/04/tumblr_p0gl7i7p5i1qjvfkco2_500.gif"],
    # Memes
    "maybe": [r"https://media.tenor.com/images/6bdd650af717980d5d898d4fd0b8ad52/tenor.gif"],
    # Misc
    "excellent": [r"https://media1.tenor.com/images/9e3409f358c9cec06061c1ec76d86d47/tenor.gif?itemid=4076853"],
}

@client.event
async def on_ready():
    # Configuring GIFs
    for i in media:
        async with aiohttp.ClientSession() as session:
            async with session.get(media[i][0]) as resp:
                if not resp.status == 200: # HTTP response status code 200 means okay
                    print(f"Could not download file: {i}")
                media[i].append(io.BytesIO(await resp.read()))
                print(f"{media[i][0]} loaded", end="; ")

    print("Bot is ready.")

# Ping
@client.command(aliases=["whatistheping", "whatstheping", "wotisleping"])
async def ping(ctx):
    await ctx.send(f"Pong! The ping is {round(client.latency * 1000)}ms.")

# Magic 8-Ball
@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
    responses = ["_Sure, honey, sure._", "You really need to ask?", "Of course, bruv.", "Bhai mai bhagwaan nahi hoon", "DUH.", "Never in a million years", "Koi chance hi nahi hai boss", "_Mayyyyybeeeee_", "Definitely", "Why even-"]
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

# GIFS
@client.command(aliases=["nice"])
async def noice(ctx):
    await ctx.send(file=discord.File(media["noice"][1], "noice.gif"))
