# Discord Bot for Notion

## Overview

This Discord bot posts updates from a designated Notion database to a dedicated channel. The bot periodically queries the Notion API for updates in the specified database. If an update is detected in Notion, the bot posts a message about it in the dedicated Discord channel. The update status is determined using the `last_edited_time` property in Notion.

## Instruction

Below are concise instructions to help you run the bot on your machine. These steps assume you have already cloned the repository and installed the necessary requirements from the `Pipfile`.

Please note that the bot will only function while the script is active. To ensure continuous usage, it is recommended to run the script on a server.

### Create a Notion Integration

Go to <https://developers.notion.com> and click `View my integrations` (or go directly to <https://www.notion.so/my-integrations>).

Create a `New integration`.

Give it any name you like, choose the desired workspace to associate with, and optionally add a logo.

Write down the `Internal Integration Token` in the `Secrets` section for later use.

In `Capabilities`, select the desired capabilities for the integration. For this bot, they should be: `Read content` and `No user information`.

### Create a Discord Bot

Open the Discord developer portal at <https://discord.com/developers/applications>.

Create a `New Application`.

Optionally fill in the `DESCRIPTION` and `TAGS`.

In the `Bot` settings, click `Reset Token` and write it down for later use.

In `OAuth2` -> `URL Generator`, select `bot` in `SCOPES` and `Send Messages` in `BOT PERMISSIONS`.

Open the `GENERATED URL` in a new browser window.

Select the server to add your new application to.

Follow the rest of the steps, and you should see a message in the `general` channel of your Discord server informing you that the application has been added.

### Set Up Tokens

In the root of the project directory, create a `.env` file with the following fields:

``` text
DISCORD_BOT_TOKEN = ''
NOTION_API_KEY = ''
DATABASE_ID = ''
DISCORD_CHANNEL_ID = ''
```

Right click on the Discord channel where you want the bot to post updates and select `Copy Channel ID`. Paste that ID into `DISCORD_CHANNEL_ID`, e.g., `DISCORD_CHANNEL_ID = '1171832436840643745'`.

Paste the Notion Integration Token into `NOTION_API_KEY`.

Copy the Notion database ID you want to track and add your integration to the database. Check this [answer](https://stackoverflow.com/questions/67728038/where-to-find-database-id-for-my-database-in-notion) on how to do that. Paste the obtained ID into `DATABASE_ID`.

Paste the Discord bot token you obtained earlier into `DISCORD_BOT_TOKEN`.

Optionally, add the poll interval in seconds, e.g., `POLL_INTERVAL = 120`. The interval should be at least 120 seconds, and it defaults to that value if not provided.

Optionally, set the log level, e.g., `LOGLEVEL = 'INFO'`. Allowed values are: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`. The default value is INFO.

### Give Channel Permission (optional)

If your desired channel is private, you will need to give permissions to the bot. Go to `Edit Channel` -> `Permissions` in Discord for the channel you want the bot to post in and make the appropriate changes.
