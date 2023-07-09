import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.presences = True
intents.typing = False
self_bot = True

bot = commands.Bot(command_prefix='.', intents=intents)

# coded by syngatelol ; syngate

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

    name = input("Enter the streaming name: ")
    url = input("Enter the Twitch URL (you can just put a random twitch if you want): ")

    await bot.change_presence(activity=discord.Streaming(name=name, url=url))

token = input("Enter your user token: ")
bot.run(token, bot = False)
