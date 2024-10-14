import logging  
from aiogram import Bot, Dispatcher, types  
from aiogram.contrib.fsm_storage.memory import MemoryStorage  
from aiogram.utils import executor  
from config import TOKEN  
from handlers import register_handlers  
from notifications import schedule_notifications  

# Настройка логирования  
logging.basicConfig(level=logging.INFO)  

# Инициализация бота и диспетчера  
bot = Bot(token=TOKEN)  
storage = MemoryStorage()  
dp = Dispatcher(bot, storage=storage)  

# Регистрация обработчиков  
register_handlers(dp)  

async def on_startup(dp):  
    # Запуск уведомлений  
    schedule_notifications()  

if __name__ == '__main__':  
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
