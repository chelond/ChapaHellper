from .main import register_all_handlers
from aiogram import types

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button_OS = types.InlineKeyboardButton('Алехин')
button_BD = types.InlineKeyboardButton('Терехин')
keyboard.add(button_BD, button_OS)

