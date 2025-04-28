# I use python3, before u start this project please install this libraries:
#pip install aiogram
#pip install python-dotenv
import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

#cons part
ALLOWED_UPDATES = ['message, edited_message']

#main part
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


async def main():
    await bot.delete_webhook(drop_pending_updates=True) #work with server URL
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())