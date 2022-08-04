from aiogram import types, Dispatcher
from config import bot


async def echo(message: types.Message):
    # await bot.send_message(message.from_user.id, message.text)
    if message.text.startswith('pin'):
        await bot.pin_chat_message(message.chat.id, message.message_id)
    x = message.text
    try:
        x = int(x)
        c = 1
    except:
        pass
        c = 0
    if c == 1:
        await bot.send_message(message.chat.id, f'{x ** 2}')
    elif c == 0:
        await bot.send_message(message.chat.id, x)
    else:
        pass


def register_echo_message(dp: Dispatcher):
    dp.register_message_handler(echo)
