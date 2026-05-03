import discord
from discord.ext import commands
from flask import Flask
from threading import Thread
import os

# --- Keep-alive server ---
app = Flask("")

@app.route("/")
def home():
    return "Bot online!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()

# --- Bot Discord ---
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot online como {bot.user}")

@bot.command()
async def oi(ctx):
    await ctx.send(f"Olá, {ctx.author.name}! 👋")

@bot.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong! Latência: {round(bot.latency * 1000)}ms")

keep_alive()
bot.run(os.environ["DISCORD_TOKEN"])
