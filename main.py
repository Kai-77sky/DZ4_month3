from aiogram.utils import executor
from config import dp
import logging
from handlers import callback, client, extra, admin, fsm_anketa


admin.register_hundleer_admin(dp)
client.register_handlers_client(dp)
fsm_anketa.register_handlers_fsmanketa(dp)
callback.register_handlers_callback(dp)
extra.register_echo_message(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
