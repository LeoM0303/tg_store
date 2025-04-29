from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command

user_private_router = Router()

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Hi, dear user")

@user_private_router.message(Command('menu'))
async def menu_cmd(message: types.Message):
    await message.reply('Menu: ')

@user_private_router.message(Command('prod'))
async def prod_cmd(message: types.Message):
    await message.reply('Products: ')


@user_private_router.message(Command('payment'))
async def payment_cmd(message: types.Message):
    await message.reply('Payment: ')


#magic filter
@user_private_router.message(F.text)
async def payment_cmd(message: types.Message):
    await message.reply('Work magic filter ')

@user_private_router.message(F.photo)
async def payment_cmd(message: types.Message):
    await message.reply('Work magic filter on photo')

@user_private_router.message(F.audio)
async def payment_cmd(message: types.Message):
    await message.reply('Work magic filter on photo')

