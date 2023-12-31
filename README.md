# eo-server-status-discord-bot
This is a Discord bot designed to monitor the status of Endless-Online servers. By default, it checks the status of the official server, but it's versatile enough to monitor any server of your choice. Simply adjust the host and/or port as necessary.

![serverpicture](examples/serverpicture.png)
<br>
![role](examples/role.png)
<br>
![serverstatus](examples/serverstatus.png)

Here are the steps to deploy this bot:

    Make sure your machine has python and the requirments installed.
    Create a Discord server (Optional).
    Create a Discord bot and take note of its api key.
    Designate a text channel named "server-status" for the bot to post updates on the server you've created/already have.
    Invite the bot to your server.
    Ensure that the bot has all necessary permissions for functionality.
    Update the config.py with your discord bots API key.
    Remember to install the 'discord.py' & 'pytz' libs. I've provided a requirements.txt.
    Run the main.py script on the machine or vps you want to host the bot from.

The bots features: It can change its name, avatar, status, and server picture in accordance with the server status. Updates are posted in the designated "server-status" text channel. Feel free to customize any aspect of the bot as you see fit, including the text channel for updates or any other characteristic.

An additional handy feature is the bot's ability to adapt to your local timezone. This can be set manually, enabling the bot to display the correct local time, and it will also alter the flag displayed when the bot posts an update.

![flags](examples/flags.png)

Enjoy the utility of this discord bot!

Creator: jc8048

