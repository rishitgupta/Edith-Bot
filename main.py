import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "")

@client.event
async def on_ready():
    print("Bot is ready.")
@client.command()
async def edith(ctx):
    await ctx.send("teri maa ki- chup")
client.run("")
