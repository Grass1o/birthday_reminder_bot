from datetime import datetime, timedelta  
import asyncio  
from aiogram import Bot  

async def schedule_notifications():  
    while True:  
        await asyncio.sleep(86400)  # Проверяем каждый день  
        notify_birthdays()  

async def notify_birthdays():  
    # Здесь реализуйте логику уведомлений.  
    # Например, проверьте базу данных и отправьте сообщения в 13:00.  
    pass
