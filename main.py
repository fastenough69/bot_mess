from telethon import TelegramClient, events
from selector import Selector

api_id = Selector.api_id
api_hash = Selector.api_hash
chat_id = Selector.chat_id
client = TelegramClient('you', api_id, api_hash)

async def main():
    await client.start(bot_token='7749696451:AAGZHskBCdXfCcOWIIi7_9sRHdUY0PN_Owo')
    await client.send_message(chat_id, 'Привет')

with client:
    client.loop.run_until_complete(main())






