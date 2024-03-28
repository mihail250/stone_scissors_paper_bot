import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

from aiogram.utils.keyboard import ReplyKeyboardBuilder

from config_data.config import load_config
from handlers import user_handlers



BOT_TOKEN = load_config().tg_bot.token



bot = Bot(BOT_TOKEN)
dp = Dispatcher()



async def main() -> None:
    
    BOT_TOKEN = load_config().tg_bot.token
    
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()
   
    dp.include_router(user_handlers.router)
    

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())