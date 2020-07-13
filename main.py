# Excellent/Ah, Noice/Nice, Cool, Toit, Woooooo/Woohoo (Ted), nikal, knockknockknock

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
    responses = ["_Sure, honey, sure._", "You really need to ask?", "Of course, bruv.", "Bhai mai bhagwaan nahi hoon", ""]
    await ctx.send(random.choice(responses))

@client.command()
async def edith(ctx):
    await ctx.send("chup ho jaa")
