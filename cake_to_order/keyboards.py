from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup)


custom_your_cake_button = KeyboardButton(text='Собрать свой авторский торт')
choose_from_catalog_button = KeyboardButton(text='Выбрать из каталога')

# skip_button = KeyboardButton(text='Пропустить')
skip_button = InlineKeyboardButton(text='Пропустить', callback_data='no_data')
without_inscription_button = InlineKeyboardButton(text='Без надписи ', callback_data='no_data')


main_page_keyboard = ReplyKeyboardMarkup(keyboard=[[custom_your_cake_button], [choose_from_catalog_button]], resize_keyboard=True, one_time_keyboard=True)
without_inscription_keyboard = InlineKeyboardMarkup(keyboard=[[custom_your_cake_button], [choose_from_catalog_button]], resize_keyboard=True, one_time_keyboard=True)
