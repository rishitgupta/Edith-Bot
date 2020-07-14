# Excellent/Ah, Noice/Nice, Cool, Toit, Woooooo/Woohoo (Ted), nikal, knockknockknock, maybeeeeeee, nooo, haie (ross), damn

import discord
from discord.ext import commands

import random

client = commands.Bot(command_prefix = "")

@client.event
async def on_ready():
    print("Bot is ready.")

@client.command(aliases=["whatistheping", "whatstheping", "wotisleping"])
async def ping(ctx):
    await ctx.send(f"Pong! The ping is {round(client.latency * 1000)}ms.")

@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
    responses = ["_Sure, honey, sure._", "You really need to ask?", "Of course, bruv.", "Bhai mai bhagwaan nahi hoon", "DUH.", "Never in a million years", "Koi chance hi nahi hai boss", "_Mayyyyybeeeee_"]
    await ctx.send(random.choice(responses))

@client.command()
async def clear(ctx, amount=0):
    if not amount == 0:
        await ctx.channel.purge(limit=amount)
    else:
        await ctx.send("> _Please enter the number of messages you'd like to clear._")

@client.command()
async def chandler(ctx, name, *, adj):
    await ctx.channel.purge(limit=1)
    await ctx.send(f"Could {name} BE any {adj}?")

@client.command()
async def edith(ctx):
    await ctx.send("> Heyo, this is Edith. \n> A bot designed to mess around with you. \n> Bask in the sheer suffering that I shall wreak upon your puny existences, \n> And a little bit of fun, too. :)")
