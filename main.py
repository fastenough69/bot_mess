from telethon import TelegramClient, events
from selector import Selector
import asyncio

api_id = Selector.api_id
api_hash = Selector.api_hash
chat_id = Selector.chat_id

client = TelegramClient('me', api_id, api_hash)
bot = TelegramClient('bot', api_id, api_hash)

@client.on(events.NewMessage(chats=chat_id))
async def bot_message(event):
    message = event.message
    me = await client.get_me()
    await bot.send_message(me.id, message.text)

async def main():
    await client.start(phone='89201001680')
    await bot.start(bot_token=Selector.bot_token)
    print(f'Отслеживаю новые сообщения в чате и отправляю в бота')
    await asyncio.gather(client.run_until_disconnected(), bot.run_until_disconnected())

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())





