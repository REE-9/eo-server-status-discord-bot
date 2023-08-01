import discord
from discord.ext import commands
import socket
from datetime import datetime
import asyncio
import pytz
import config

# Hi, I hope you enjoy using my server status discord bot for endless-online
# Creator: jc8048

# --- notes ---
# Remember when you create your discord bot to give it all the permissions needed.
# Make sure to replace the placeholder text in config.py and paste in your discord bot api key.
# Errors will probably be permission related if not setup correctly.
# This will work with any of the EO Servers just replace the host & or port.
# To keep this running 24/7 you will either need to have it on a machine that is on all the time or rent a VPS or something.
# the only libs that don't come with python here you will need to install are 'discord' & 'pytz'
# --- notes ---


intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
bot.previous_status = None

flag_timezones = {
    "Europe/London": ":flag_gb:",
    "Europe/Amsterdam": ":flag_nl:",
    "Europe/Warsaw": ":flag_pl:",
    "Europe/Moscow": ":flag_ru:",
    "America/Los_Angeles": ":flag_us:",
    "America/Toronto": ":flag_ca:",
    "America/Sao_Paulo": ":flag_br:",
    "Australia/Sydney": ":flag_au:",
    "Asia/Tokyo": ":flag_jp:",
    # ... add more countries flags here if you want
}

# This is your manually set timezone
manual_timezone = "Europe/London"

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

    # Make sure you've made a text channel called 'server-status'
    # Get the server-status channel by name
    channel = discord.utils.get(bot.get_all_channels(), name='server-status')

    if channel is not None:
        await check_server_status(channel)
        bot.loop.create_task(check_server_periodically(channel))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Check if the message is in the server-status channel
    if message.channel.name == 'server-status':
        await check_server_status(message.channel)

    await bot.process_commands(message)

# Function to check server status
async def check_server_status(channel):
    hostname = 'game.endless-online.com'
    port = 8078

    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout of 1 seconds
        sock.settimeout(1)

        # Attempt to connect to the host and port
        result = sock.connect_ex((hostname, port))

        flag = flag_timezones.get(manual_timezone, ":flag_gb:")  # default to UK flag
        timestamp = datetime.now(pytz.timezone(manual_timezone)).strftime(f"%I:%M:%S %p | {flag} | %d-%m-%Y")

        if result == 0:
            if bot.previous_status != 'online':
                # Set online icon
                with open('pictures/online.png', 'rb') as icon_file:
                    icon = icon_file.read()
                    guild = channel.guild
                await guild.edit(icon=icon)
                await bot.user.edit(avatar=icon)
                # Delete previous message if it exists
                async for message in channel.history():
                    if message.author == bot.user:
                        await message.delete()

                await channel.send(f"{timestamp}\n{hostname}:{port}\n:white_check_mark::white_check_mark::white_check_mark: ONLINE :white_check_mark::white_check_mark::white_check_mark:")
                await bot.change_presence(status=discord.Status.online)
                await bot.guilds[0].me.edit(nick="endless-online")
            bot.previous_status = 'online'
        else:
            if bot.previous_status != 'offline':
                # Set offline icon
                with open('pictures/offline.png', 'rb') as icon_file:
                    icon = icon_file.read()
                    guild = channel.guild
                await guild.edit(icon=icon)
                await bot.user.edit(avatar=icon)
                # Delete previous message if it exists
                async for message in channel.history():
                    if message.author == bot.user:
                        await message.delete()

                await channel.send(f"{timestamp}\n{hostname}:{port}\n:x::x::x: OFFLINE :x::x::x:")
                await bot.change_presence(status=discord.Status.dnd)
                await bot.guilds[0].me.edit(nick="endless-offline")
            bot.previous_status = 'offline'

        # Close the socket
        sock.close()

    except socket.error as e:
        if bot.previous_status != 'offline':
            # Set offline icon
            with open('pictures/offline.png', 'rb') as icon_file:
                icon = icon_file.read()
                guild = channel.guild
            await guild.edit(icon=icon)
            await bot.user.edit(avatar=icon)

            # Delete previous message if it exists
            async for message in channel.history():
                if message.author == bot.user:
                    await message.delete()

            await channel.send(f"[{timestamp}] Error occurred: {e}")
            await bot.change_presence(status=discord.Status.dnd)
            await bot.guilds[0].me.edit(nick="endless-offline")
        bot.previous_status = 'offline'

# Function to periodically check server status
async def check_server_periodically(channel):
    while True:
        await check_server_status(channel)
        await asyncio.sleep(10)  # Wait for 10 seconds before checking the server again

bot.run(config.API_KEY)