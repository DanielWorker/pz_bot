import asyncio
import logging

from telethon import TelegramClient, events

from config import API_ID, API_HASH, TOKEN, ALLOWED_USERS
from server_functions import get_server_status, start_server, stop_server, save_server, start_message

logger = logging.getLogger(__name__)

client = TelegramClient('bot', API_ID, API_HASH, base_logger='telegram')

# @client.on(events.NewMessage(pattern='/status'))
# async def status_handler(event):
#     await event.respond(get_server_status())


@client.on(events.NewMessage(pattern='^/start$', from_users=ALLOWED_USERS))
async def start_handler(event):
    await event.respond(start_message())


@client.on(events.NewMessage(pattern='^/start_server$', from_users=ALLOWED_USERS))
async def start_handler(event):
    await event.respond(start_server())


@client.on(events.NewMessage(pattern='/stop', from_users=ALLOWED_USERS))
async def stop_handler(event):
    await event.respond(stop_server())


@client.on(events.NewMessage(pattern='/save', from_users=ALLOWED_USERS))
async def stop_handler(event):
    await event.respond(save_server())


async def run_bot():
    await client.start(bot_token=TOKEN)
    logger.info('Bot started')
    while True:
        try:
            await client.run_until_disconnected()
        except Exception as e:
            logger.error(f"Bot crashed: {e}")
            await asyncio.sleep(5)


if __name__ == '__main__':
    try:
        asyncio.run(run_bot())
    except KeyboardInterrupt:
        logger.warning("KeyboardInterrupt exception caught")
