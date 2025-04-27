# I use python3, before u start this project please install this libraries:
#pip install aiogram
#pip install python-dotenv
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

bot = Bot(token="")
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Hello world")

@dp.message()
async def echo(message: types.Message):
    await message.reply(message.text)


async def main():
    await dp.start_polling(bot)


asyncio.run(main())