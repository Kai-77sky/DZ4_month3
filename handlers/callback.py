from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

from config import bot


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    markup.add(button_call_2)
    question = "1 What next?"
    answers = [
        '2', '3', '4', '5'
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='Ват некст',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )


async def quiz_3(call: types.CallbackQuery):
    quest = "'сколько? 4+5 "
    answers1 = [
        '2'
        '3'
        '4'
        '5'
        '6+3'
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=quest,
        options=answers1,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='Ват некст',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )


async def vetka_good1(call:types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_8 = InlineKeyboardButton("good", callback_data='button_call_8')
    button_call_9 = InlineKeyboardButton("bad", callback_data='button_call_9')
    markup.add(button_call_8, button_call_9)
    await bot.send_message(call.message.chat.id, '.', reply_markup=markup)


def register_handlers_callback(dp: Dispatcher):
     dp.register_callback_query_handler(quiz_2, lambda call: call.data == "button_call_1")
     dp.register_callback_query_handler(quiz_3, lambda call: call.data == "button_call_2")
     dp.register_callback_query_handler(vetka_good1, lambda call: call.data == "button_call_6")