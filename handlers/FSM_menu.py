from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import bot

from database import bot_db


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


async def fsm_start(message: types.Message):
    if message.chat.type == "private":
        await FSMAdmin.photo.set()
        await message.answer(f"Салам {message.from_user.full_name} "
                             f"скинь фотку...")
    else:
        await message.reply("Пиши в личку!")


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer("название блюдо")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("описание")


async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.answer("price")


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
        await bot.send_photo(message.from_user.id, data['photo'],
                             caption=f"name: {data['name']}\n"
                                     f"description: {data['description']}\n"
                                     f"price: {data['price']}"
                             )
        await bot_db.sql_insert(state)
        await state.finish()
        await message.answer("Free)")


async def cancel_registration(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
        await message.answer("Cancel")


async def complete_delete(call: types.CallbackQuery):
    await bot_db.sql_delete(call.data.replace("delete ", ""))
    await call.answer(text=f'{call.data.replace("delete ", "")} deleted',
                      show_alert=True)


async def delete_data(message: types.Message):
    selected_data = await bot_db.sql_casual_select()
    for result in selected_data:
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=result[0],
            caption=f'name: {result[1]}\n description: {result[2]}\n price: {result[3]}',
            reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton(
                    f'delete: {result[1]}',
                    callback_data=f'delete {result[1]}'
                )
            )
        )


def register_handlers_menu(dp: Dispatcher):
    dp.register_message_handler(cancel_registration, state="*", commands='cancel')
    dp.register_message_handler(cancel_registration,
                                Text(equals='cancel', ignore_case=True), state="*")

    dp.register_message_handler(fsm_start, commands=['menu'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo,
                                content_types=['photo'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_callback_query_handler(
        complete_delete,
        lambda call: call.data and call.data.startswith("delete "))
    dp.register_message_handler(delete_data, commands=['delete'])
