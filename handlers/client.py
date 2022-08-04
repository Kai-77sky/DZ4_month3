from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton

from config import bot


async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'Ассалам Алейкум {message.from_user.full_name}')


async def quiz(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)
    question = "A What next? "
    answer = [
        'B', "C", "D", "E"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="хм",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def vetka(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_6 = InlineKeyboardButton("Хорошо", callback_data='button_call_6')
    button_call_7 = InlineKeyboardButton("плохо", callback_data='button_call_7')
    markup.add(button_call_6, button_call_7)
    await bot.send_message(message.chat.id, 'How are you?', reply_markup=markup)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(quiz,commands=['quiz'])
    dp.register_message_handler(vetka,commands=['vetka'])
