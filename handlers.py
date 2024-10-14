from aiogram import types  
from aiogram.dispatcher import Dispatcher  
from keyboards import get_buttons  
from models import add_employee, remove_employee, get_employees  
from utils import is_valid_date  

async def cmd_start(message: types.Message):  
    await message.answer("Добро пожаловать! Используйте кнопки для взаимодействия.", reply_markup=get_buttons())  

async def show_employees(message: types.Message):  
    employees = get_employees(message.from_user.id)  
    await message.answer("\n".join(employees) if employees else "Список сотрудников пуст.")  

async def add_employee_handler(message: types.Message):  
    await message.answer("Введите ФИО и дату рождения в формате: Фамилия Имя Отчество ДД.ММ.ГГГГ")  

async def handle_employee_addition(message: types.Message):  
    data = message.text.split()  
    if len(data) == 4 and is_valid_date(data[3]):  
        name = ' '.join(data[:-1])  
        date_of_birth = data[-1]  
        add_employee(message.from_user.id, name, date_of_birth)  
        await message.answer("Сотрудник успешно добавлен!")  
    else:  
        await message.answer("Ошибка: проверьте формат ФИО и даты рождения.")  

def register_handlers(dp: Dispatcher):  
    dp.register_message_handler(cmd_start, commands=['start'])  
    dp.register_message_handler(show_employees, text="Показать список ваших сотрудников")  
    dp.register_message_handler(add_employee_handler, text="Добавить день рождения нового сотрудника")  
    dp.register_message_handler(handle_employee_addition)
