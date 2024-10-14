from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  

def get_buttons():  
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)  
    keyboard.add(KeyboardButton("Показать список ваших сотрудников"))  
    keyboard.add(KeyboardButton("Добавить день рождения нового сотрудника"))  
    keyboard.add(KeyboardButton("Как работают уведомления"))  
    return keyboard
