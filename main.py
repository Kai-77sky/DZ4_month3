from aiogram.utils import executor
from config import dp
import logging

from database import bot_db
from handlers import callback, client, extra, admin, FSM_menu


async def on_startup(_):
    bot_db.sql_create()
    print("Bot is online")

admin.register_hundleer_admin(dp)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
FSM_menu.register_handlers_menu(dp)
extra.register_echo_message(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True,on_startup=on_startup)