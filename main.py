# bot.py
import os

import discord
import random
from discord import app_commands
from discord.ext import commands
from scrape import to_scrape
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('bot_token')
GUILD = os.getenv('guild_id')

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
tree = bot.tree

@bot.event
async def on_ready():
    print("Boot is ready")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

@bot.tree.command(name='word', description='get a random word')
async def hello(interaction: discord.Interaction):
    name, desc, example = to_scrape()
    await interaction.response.send_message(f"Дума: {name}\nОписание: {desc}\nПример: {example}")


bot.run(TOKEN)
