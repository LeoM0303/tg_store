# I use python3, before u start this project please install this libraries:
#pip install aiogram
#pip install python-dotenv
import asyncio

from aiogram import Bot, Dispatcher, types


bot = Bot(token="")

dp = Dispatcher()

async def main():
    await dp.start_polling(bot)


asyncio.run(main())