from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup)


custom_your_cake_button = KeyboardButton(text='Собрать свой авторский торт')
choose_from_catalog_button = KeyboardButton(text='Выбрать из каталога')

# skip_button = KeyboardButton(text='Пропустить')
skip_button = InlineKeyboardButton(text='Пропустить', callback_data='no_data')
without_inscription_button = InlineKeyboardButton(text='Без надписи ', callback_data='no_data')
time_button_1 = InlineKeyboardButton(text='11:00 - 15:00', callback_data='11:00 - 15:00')
time_button_2 = InlineKeyboardButton(text='15:00 - 19:00', callback_data='15:00 - 19:00')
# go_home_button = InlineKeyboardButton(text='Вернуться в начало', callback_data='Вернуться в начало')
go_home_button = KeyboardButton(text='Вернуться в начало')
about_us_button = KeyboardButton(text='О нас') #'Адрес, название компании'


main_page_keyboard = ReplyKeyboardMarkup(keyboard=[[custom_your_cake_button], [choose_from_catalog_button]], resize_keyboard=True, one_time_keyboard=True)
without_inscription_keyboard = InlineKeyboardMarkup(inline_keyboard=[[without_inscription_button]])
skip_keyboard = InlineKeyboardMarkup(inline_keyboard=[[skip_button]])
time_selecting_keyboard = InlineKeyboardMarkup(inline_keyboard=[[time_button_1, time_button_2]])
# go_home_keyboard = InlineKeyboardMarkup(inline_keyboard=[[go_home_button]])
go_home_keyboard = ReplyKeyboardMarkup(keyboard=[[go_home_button]], resize_keyboard=True)
