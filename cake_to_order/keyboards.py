from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup)


custom_your_cake_button = KeyboardButton(text='Собрать свой авторский торт')
choose_from_catalog_button = KeyboardButton(text='Выбрать из каталога')

one_level_button = KeyboardButton(text='1 уровень (+400 р.)')
two_levels_button = KeyboardButton(text='2 уровня (+750 р.)')
three_levels_button = KeyboardButton(text='3 уровня (+1 100 р.)')

round_button = KeyboardButton(text='Круг (+400 р.)')
square_button = KeyboardButton(text='Квадрат (+600 р.)')
rectangular_button = KeyboardButton(text='Прямоугольник (+1 000 р.)')

white_sauce_button = KeyboardButton(text='Белый соус (+200 р.)')
caramel_syrup_button = KeyboardButton(text='Карамельный сироп (+180 р.)')
maple_syrup_button = KeyboardButton(text='Кленовый сироп (+200 р.)')
strawberry_syrup_button = KeyboardButton(text='Клубничный сироп (+300 р.)')
blueberry_syrup_button = KeyboardButton(text='Черничный сироп (+350 р.)')
milk_chocolate_button = KeyboardButton(text='Молочный шоколад (+200 р.)')

skip_button = KeyboardButton(text='Пропустить')


main_page_keyboard = ReplyKeyboardMarkup(keyboard=[[custom_your_cake_button], [choose_from_catalog_button]], resize_keyboard=True)
level_choosing_keyboard = ReplyKeyboardMarkup(keyboard=[[one_level_button], [two_levels_button], [three_levels_button]], resize_keyboard=True)
shape_choosing_keyboard = ReplyKeyboardMarkup(keyboard=[[round_button], [square_button], [rectangular_button]], resize_keyboard=True)
topping_choosing_keyboard = ReplyKeyboardMarkup(keyboard=[[white_sauce_button], [caramel_syrup_button], [maple_syrup_button], [strawberry_syrup_button], [blueberry_syrup_button], [milk_chocolate_button], [skip_button]], resize_keyboard=True)
