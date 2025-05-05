from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f

user_private_router = Router()

#main commands
@user_private_router.message(F.text.lower().contains('hello') | (F.text.lower() == 'hey'))
@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Hi, dear user")

@user_private_router.message(or_f(Command('menu'), (F.text.lower() == 'menu')))
async def menu_cmd(message: types.Message):
    await message.reply('Menu: ')

@user_private_router.message(or_f(Command('prod'), (F.text.lower() == 'product')))
async def prod_cmd(message: types.Message):
    await message.reply('Products: ')

@user_private_router.message(or_f(Command('payment'), (F.text.lower() == 'delivery point')))
async def payment_cmd(message: types.Message):
    await message.reply('We work for this: ')


#magic filter
@user_private_router.message(F.text.lower() == 'apple')
async def payment_cmd(message: types.Message):
    await message.reply("Right now, we haven't apple production")

@user_private_router.message(F.text)
async def payment_cmd(message: types.Message):
    await message.reply('Work magic filter ')

@user_private_router.message(F.photo)
async def payment_cmd(message: types.Message):
    await message.reply('Work magic filter on photo')

@user_private_router.message(F.audio)
async def payment_cmd(message: types.Message):
    await message.reply('Work magic filter on photo')
