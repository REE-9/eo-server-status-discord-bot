# eo-server-status-discord-bot
This is a Discord bot designed to monitor the status of Endless-Online servers. By default, it checks the status of the official server, but it's versatile enough to monitor any server of your choice. Simply adjust the host and/or port as necessary.

Here are the steps to deploy this bot:

    Create a Discord server.
    Create a Discord bot and take note of its api key.
    Designate a text channel named "server-status" for the bot to post updates on the server you've created/already have.
    Invite the bot to it.
    Ensure that the bot has all necessary permissions for functionality.
    Update the config.py with your discord bots API key.
    Remember to install the 'discord.py' & 'pytz' libs. I've provided a requirements.txt.
    Run the main.py script on the machine or vps you want to host the bot from.

The bots features: It can change its name, avatar, status, and server picture in accordance with the server status. Updates are posted in the designated "server-status" text channel. Feel free to customize any aspect of the bot as you see fit, including the text channel for updates or any other characteristic.

An additional handy feature is the bot's ability to adapt to your local timezone. This can be set manually, enabling the bot to display the correct local time, and it will also alter the flag displayed when the bot posts an update.

Enjoy the utility of this discord bot!

Creator: jc8048

