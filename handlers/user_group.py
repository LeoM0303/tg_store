from string import punctuation

from aiogram import F, types, Router

user_group_router = Router()

restricted_words = {'fuck', 'shit', 'your mom'}

def cleaner_text(text: str):
    return text.translate(str.maketrans('', '', punctuation))

@user_group_router.message()
async def start_cmd(message: types.Message):
    if restricted_words.intersection(message.text.lower().split()):
        await message.answer(f'{message.from_user.username}, please be more claim')
        await message.delete()