from aiogram import types, Router
from aiogram.filters import CommandStart


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Hi, dear user")

@dp.message()
async def echo(message: types.Message):
    await message.reply(message.text)

