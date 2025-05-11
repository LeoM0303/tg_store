# I use python3, before u start this project please install this libraries:
#pip install aiogram
#pip install python-dotenv
import asyncio
import os

from aiogram import Bot, Dispatcher, types
from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())

#imports from file
from handlers.user_private import user_private_router
from command.bot_command_list import private


#cons part
ALLOWED_UPDATES = ['message', 'edited_message']

#main part
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

#include router
dp.include_routers(user_private_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True) #work with server URL
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats()) command for deleting menu
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())