# Discord Bot for Notion

## Overview

Discord bot that posts Notion database updates to a dedicated channel.

Bot periodically queries Notion API for updates in the designated database. If there is an update in Notion, bot posts a message about it in a dedicated Discord channel. Status (update) is determined using `last_edited_time` property in Notion.

## Instruction

### Create Notion Integration

Go to <https://developers.notion.com> and click `View my integrations` (or go directly to <https://www.notion.so/my-integrations>).

Create `New integration`.

Give it any name you like, choose the desired workspace to associate with, and optionally add a logo.

In `Secrets` write down `Internal Integration Token` for later.

In `Capabilities` select the desired capabilities for the integration. In the case of this bot they should be: `Read content` and `No user information`.

### Create Discord Bot

Open Discord developer portal at <https://discord.com/developers/applications>.

Create `New Application`.

Optionally fill in `DESCRIPTION` and `TAGS`.

In `Bot` settings `Reset Token` and write it down for later.

In `OAuth2` -> `URL Generator` select `bot` in `SCOPES` and `Send Messages` in `BOT PERMISSIONS`.

Open the `GENERATED URL` in a new browser window.

Select the server to add your new application to.

Follow the rest of the steps and you should see a message in the `general` channel of your Discord server informing you that application has been added.

### Set Up Tokens

In the root of this directory create `.env` file with following fields:

``` text
DISCORD_BOT_TOKEN = ''
NOTION_API_KEY = ''
DATABASE_ID = ''
DISCORD_CHANNEL_ID = ''
```

Right click on the Discord channel where you want the bot to post updates to and `Copy Channel ID`. Paste that ID into `DISCORD_CHANNEL_ID`, e.g., `DISCORD_CHANNEL_ID = '1171832436840643745'`.

Copy the Notion database ID you want to track and add your integration to the database. Check this [answer](https://stackoverflow.com/questions/67728038/where-to-find-database-id-for-my-database-in-notion) on how to find it. Paste that ID into `DATABASE_ID`.

Paste Discord bot token you obtained earlier into `DISCORD_BOT_TOKEN`.

Paste Notion Integration Token into `NOTION_API_KEY`.
