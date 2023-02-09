
import os

import discord
from discord import app_commands
from discord.ext import commands
import pandas as pd
#from dotenv import load_dotenv
#from wz_stats_tracker import getUserData

#load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#bot = discord.Client(intents=discord.Intents.default())
bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())
#tree = app_commands.CommandTree(bot)
active_guild = None
#For functions that execute on an event
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    text_channel_list = []
    #for current_guild in bot.guilds:
    #    if current_guild.name == GUILD:
    #        active_guild = current_guild
    #        #print(active_guild.id)
    #        bot.tree.copy_global_to(guild=active_guild)
    #        print(f'{bot.user} is connected to the following guild:\n' f'{current_guild.name}(id: {current_guild.id})')
    #        for channel in current_guild.text_channels:
    #            await channel.send(f'Bot is connected to channel: {channel}')
    #            text_channel_list.append(channel)
    #        break
    active_guild = bot.get_guild(1072618094201143378)
    #print(active_guild.id)
    bot.tree.copy_global_to(guild=active_guild)
    print(f'{bot.user} is connected to the following guild:\n' f'{active_guild.name}(id: {active_guild.id})')
    for channel in active_guild.text_channels:
        await channel.send(f'Bot is connected to channel: {channel}')
        text_channel_list.append(channel)
    try:
        await bot.tree.sync(guild=active_guild)
    except:
        print("sync failed")
    
@bot.event
async def on_member_join(member):
    channel = bot.get_channel('general')
    await channel.send(f'Hi {member.name}, welcome to The Kingdom! Get some dubs and bring glory to the Kingdom!')

#For functions that execute when a command is called
@bot.command(name = "sync", description="manual sync command", guild = 1072618094201143378)
async def sync(ctx):
    bot.tree.copy_global_to(guild=active_guild)
    fmt = await ctx.bot.tree.sync(guild=ctx.guild)
    await ctx.send(f"synced {len(fmt)} commands to the current guild")
    return

@bot.command(name = "connect_activision", description = "Connect discord username with activision username", guild=1072618094201143378)
async def connect_activision(ctx):
    await ctx.send("Please provide your activisionID")

    def check(m):
        return m.author == ctx.author

    msg = await bot.wait_for("message", check=check)

    await ctx.send(f"Thank You {ctx.author}, attempting to connect to activision...")

    try:
        #call wz api to check for connection
        print(f"calling api on {msg}")
    except:
        await ctx.send("Connection failed. Please call this function again and make sure you correctly entered your activision id. If it doesn't work then idk, activision's stuff might be messed up.")
    else:
        await ctx.send("Connection Succeeded. Happy Gaming!")
        user_info = pd.DataFrame(columns=['discord_user', 'activision_user'])
        user_info.to_csv('activition_users.csv',mode='a', index=False, header=False)
        #get stats overview
    

bot.run(TOKEN)