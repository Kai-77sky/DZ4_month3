import random

from aiogram import types, Dispatcher
from config import bot, ADMIN


async def ban(message:types.Message):
    if message.chat.type != "private":
        if message.from_user.id not in ADMIN:
            await message.answer("Ты не Админ!")
        elif not message.reply_to_message:
            await message.answer("команда должно быть ответом на сообщение!")
        else:
            pass


async def game(message:types.Message):
    if message.from_user.id in ADMIN:
        emojies = ['⚽️', '🏀', '🎯', '🎳', '🎰', '🎲']
        rand_game = random.choice(emojies)
        await bot.send_dice(message.chat.id, emoji=rand_game)


def register_hundleer_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['admin'])
    dp.register_message_handler(game, commands=['game'])
