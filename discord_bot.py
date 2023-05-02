import os
import asyncio
from datetime import datetime
import logging

from discord import Intents
from discord.ext import commands
from notion_client import Client
from dotenv import load_dotenv

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

# Load environment variables from .env file
load_dotenv()

# Retrieve values from environment variables
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
DATABASE_ID = os.getenv("DATABASE_ID")
DISCORD_CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

# Create default intents and disable members intent
intents = Intents.default()

# Initialize the Discord bot with the specified intents
bot = commands.Bot(command_prefix="!", intents=intents)

# Initialize the Notion client
notion = Client(auth=NOTION_API_KEY)

# Store the last checked timestamp
last_checked = datetime.utcnow().replace(microsecond=0).isoformat()


# Helper function to retrieve pages from Notion database
async def get_notion_pages():
    global last_checked
    try:
        pages = notion.databases.query(
            **{
                "database_id": DATABASE_ID,
                "filter": {
                    "and": [
                        {
                            "timestamp": "last_edited_time",
                            "last_edited_time": {"after": last_checked},
                        }
                    ]
                },
            }
        ).get("results")
        last_checked = datetime.utcnow().replace(microsecond=0).isoformat()
        logger.info(f"Last checked at: {last_checked}")
        logger.debug(pages)
        return pages
    except Exception as e:
        logger.error(f"Error fetching pages from Notion: {e}")
        return []


# Helper function to format Notion pages as Discord messages
def format_page_message(page):
    title = page["properties"]["Name"]["title"][0]["text"]["content"]
    message = f"**New Update:** {title}\n"
    return message


async def poll_notion_database():
    while True:
        pages = await get_notion_pages()
        channel = bot.get_channel(DISCORD_CHANNEL_ID)
        for page in pages:
            message = format_page_message(page)
            try:
                await channel.send(message)
            except Exception as e:
                logger.error(f"Error sending message to Discord: {e}")
        await asyncio.sleep(120)  # Poll every N seconds


@bot.event
async def on_ready():
    logger.info(f"{bot.user} is now online!")
    try:
        await poll_notion_database()
    except Exception as e:
        logger.error(f"Error polling Notion database: {e}")


if __name__ == "__main__":
    bot.run(DISCORD_BOT_TOKEN)
