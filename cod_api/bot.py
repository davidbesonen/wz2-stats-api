
import os

import discord
from discord.ext import commands
#from dotenv import load_dotenv
#from wz_stats_tracker import getUserData

#load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.default())
bot = commands.Bot(command_prefix='$')

#For functions that execute on an event
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
    channel = client.get_channel('general')
    await channel.send(
        f'Hi {member.name}, welcome to The Kingdom! Get some dubs and bring glory to the Kingdom!'
    )

#For funtions that execute when a command is called
@bot.command()
async def connect_activision(ctx):
    await ctx.send("Please provide your activisionID")

    def check(m):
        return m.content == "hello" and m.author == ctx.author

    msg = await bot.wait_for("message", check=check)

    await ctx.send(f"Thank You {ctx.author}, attempting to connect to activision...")

    try:
        #call wz api to check for connection
        print(f"calling api on {msg}")
    except:
        await ctx.send("Connection failed. Please call this function again and make sure you correctly entered your activision id. If it doesn't work then idk, activision's stuff might be messed up.")
    else:
        await ctx.send("Connection Succeeded. Happy Gaming!")
        #gets stats overview




client.run(TOKEN)