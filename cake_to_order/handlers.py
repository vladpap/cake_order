from cake_to_order.settings import TG_BOT_TOKEN
from keyboards import (main_page_keyboard, skip_button, skip_keyboard,
                       without_inscription_keyboard, time_selecting_keyboard,
                       go_home_keyboard)
from texts import TEXTS

import os
from datetime import date, timedelta
from aiogram import Bot, Router
from aiogram.types import (Message, KeyboardButton, InlineKeyboardButton,
                           InlineKeyboardMarkup, CallbackQuery,
                           ReplyKeyboardRemove, FSInputFile)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.filters import CommandStart, Text, StateFilter
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cake_to_order.settings')
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
import django
from django.conf import settings

if not settings.configured:
    django.setup()

from main_app.models import ClientUser


bot = Bot(TG_BOT_TOKEN)
router = Router()


class FSM(StatesGroup):
    # start_page_state = State()
    # custom_cake_state = State()
    # level_choosing_state = State()
    shape_choosing_state = State()
    topping_choosing_state = State()
    berries_choosing_state = State()
    decor_choosing_state = State()
    add_inscription_state = State()
    add_comment_state = State()
    input_address_state = State()
    input_date_state = State()
    input_time_state = State()
    show_order_state = State()


cake_pic = FSInputFile('pictures/Tort.png')
cake_levels = FSInputFile('pictures/Levels.png')
cake_shape = FSInputFile('pictures/figure.png')
toppings_photo = FSInputFile('pictures/topping.png')
berries_photo = FSInputFile('pictures/berries.png')
decor_photo = FSInputFile('pictures/decor.png')
inscription_photo = FSInputFile('pictures/Text.png')
ready_cakes_photo = FSInputFile('pictures/all.png')


levels = {1: '1 уровень (+400 р.)',
          2: '2 уровня (+750 р.)',
          3: '3 уровня (+1 100 р.', }
shapes = {1: '🟡 Круг (+400 р.)',
          2: '🟨 Квадрат (+600 р.)',
          3: '🟨🟨 Прямоугольник (+1 000 р.)', }
toppings = {1: 'Белый соус (+200 р.)',
            2: 'Карамельный сироп (+180 р.)',
            3: 'Кленовый сироп (+200 р.)',
            4: 'Клубничный сироп (+300 р.)',
            5: 'Черничный сироп (+350 р.)',
            6: 'Молочный шоколад (+200 р.)', }
berries = {1: 'Ежевика (+400 р.)',
           2: 'Малина (+300 р.)',
           3: '🫐 Голубика (+450 р.)',
           4: '🍓 Клубника (+500 р.)', }
decors = {1: 'Фисташки (+300 р.)',
          2: 'Безе (+400 р.)',
          3: 'Фундук (+350 р.)',
          4: 'Пекан (+300 р.)',
          5: 'Маршмеллоу (+200 р.)',
          6: 'Марципан (+280 р.)', }
ready_cakes = {1: 'Торт 1',
               2: 'Торт 2',
               3: 'Торт 3',
               4: 'Торт 4',
               5: 'Торт 5',
               6: 'Торт 6',
               7: 'Торт 7',
               8: 'Торт 8', }


@router.message(CommandStart())
@router.message(Text(text='Вернуться в начало'))
async def process_start_command(message: Message, state: FSMContext):
    await state.clear()
    # state.set_state(default_state)
    await bot.send_photo(chat_id=message.chat.id, photo=cake_pic,
                         caption=TEXTS['greeting'],
                         reply_markup=main_page_keyboard)


@router.message(Text(text='Собрать свой авторский торт'))
async def process_custom_your_cake_button(message: Message, state: FSMContext):
    kb_builder = InlineKeyboardBuilder()
    buttons = [InlineKeyboardButton(text=levels[level], callback_data=level) for level in levels]
    kb_builder.row(*buttons, width=1)
    await bot.send_photo(chat_id=message.chat.id, photo=cake_levels,
                         caption='Сколько уровней будет?',
                         reply_markup=kb_builder.as_markup())
    await state.set_state(FSM.shape_choosing_state)


@router.callback_query(StateFilter(FSM.shape_choosing_state))
async def process_level_choosing(callback: CallbackQuery, state: FSMContext):
    await state.update_data(level_id=callback.data)
    kb_builder = InlineKeyboardBuilder()
    buttons = [InlineKeyboardButton(text=shapes[shape], callback_data=shape) for shape in shapes]
    kb_builder.row(*buttons, width=1)
    await bot.send_photo(chat_id=callback.from_user.id, photo=cake_shape,
                         caption='Какой формы будет Ваш торт?',
                         reply_markup=kb_builder.as_markup())
    await state.set_state(FSM.topping_choosing_state)


@router.callback_query(StateFilter(FSM.topping_choosing_state))
async def process_shape_choosing(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.update_data(shape_id=callback.data)
    kb_builder = InlineKeyboardBuilder()
    buttons = [InlineKeyboardButton(text=toppings[topping], callback_data=topping) for topping in toppings]
    kb_builder.row(*buttons, width=1)
    kb_builder.row(skip_button)
    await bot.send_photo(chat_id=callback.from_user.id, photo=toppings_photo,
                         caption='Выбрать топинг',
                         reply_markup=kb_builder.as_markup())
    await state.set_state(FSM.berries_choosing_state)


@router.callback_query(StateFilter(FSM.berries_choosing_state))
async def process_toping_choosing(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.update_data(topping_id=callback.data)
    kb_builder = InlineKeyboardBuilder()
    buttons = [InlineKeyboardButton(text=berries[berry], callback_data=berry) for berry in berries]
    kb_builder.row(*buttons, width=1)
    kb_builder.row(skip_button)
    await bot.send_photo(chat_id=callback.from_user.id, photo=berries_photo,
                         caption='Добавить ягод',
                         reply_markup=kb_builder.as_markup())
    await state.set_state(FSM.decor_choosing_state)


@router.callback_query(StateFilter(FSM.decor_choosing_state))
async def process_berry_choosing(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.update_data(berry_id=callback.data)
    kb_builder = InlineKeyboardBuilder()
    buttons = [InlineKeyboardButton(text=decors[decor], callback_data=decor) for decor in decors]
    kb_builder.row(*buttons, width=1)
    kb_builder.row(skip_button)
    await bot.send_photo(chat_id=callback.from_user.id, photo=decor_photo,
                         caption='Выбрать декор',
                         reply_markup=kb_builder.as_markup())
    await state.set_state(FSM.add_inscription_state)


@router.callback_query(StateFilter(FSM.add_inscription_state))
async def process_decor_choosing(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.update_data(decor_id=callback.data)
    await bot.send_photo(chat_id=callback.from_user.id, photo=inscription_photo,
                         caption='Мы можем разместить на торте любую надпись\nОтправьте сообщение с надписью',
                         reply_markup=without_inscription_keyboard)
    await state.set_state(FSM.add_comment_state)


@router.callback_query(StateFilter(FSM.add_comment_state))
async def process_without_inscription_button(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.update_data(inscription=callback.data)
    await bot.send_message(chat_id=callback.from_user.id,
                           text='Добавьте комментарий к заказу',
                           reply_markup=skip_keyboard)
    await state.set_state(FSM.input_address_state)


@router.message(StateFilter(FSM.add_comment_state))
async def process_inscription_input(message: Message, state: FSMContext):
    await state.update_data(inscription=message.text)
    await message.answer(text='Добавьте комментарий к заказу',
                         reply_markup=skip_keyboard)
    await state.set_state(FSM.input_address_state)


@router.callback_query(StateFilter(FSM.input_address_state))
async def process_without_comment_button(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.update_data(comment=callback.data)
    await bot.send_message(chat_id=callback.from_user.id,
                           text='Введите адрес доставки')
    await state.set_state(FSM.input_date_state)


@router.message(StateFilter(FSM.input_address_state))
async def process_comment_input(message: Message, state: FSMContext):
    await state.update_data(comment=message.text)
    await message.answer(text='Введите адрес доставки')
    await state.set_state(FSM.input_date_state)


@router.message(StateFilter(FSM.input_date_state))
async def process_address_input(message: Message, state: FSMContext):
    await state.update_data(address=message.text)

    day = date.today()
    dates = []
    for _ in range(8):
        day += timedelta(days=1)
        dates.append(day)
    dates = [f'{date.day}.{str(date.month).zfill(2)}' for date in dates]

    kb_builder = InlineKeyboardBuilder()
    buttons = [InlineKeyboardButton(text=date, callback_data=date) for date in dates]
    kb_builder.row(*buttons, width=4)
    await message.answer(text='Выберите дату доставки',
                         reply_markup=kb_builder.as_markup())
    await state.set_state(FSM.input_time_state)


@router.callback_query(StateFilter(FSM.input_time_state))
async def process_date_input(callback: CallbackQuery, state: FSMContext):
    await state.update_data(date=callback.data)
    await bot.send_message(chat_id=callback.from_user.id,
                           text='Выберите время',
                           reply_markup=time_selecting_keyboard)
    await state.set_state(FSM.show_order_state)


@router.callback_query(StateFilter(FSM.show_order_state))
async def process_time_input(callback: CallbackQuery, state: FSMContext):
    await state.update_data(time=callback.data)
    cake = await state.get_data()
    await state.clear()
    await bot.send_message(chat_id=callback.from_user.id,
                           text=f'Ваш заказ:\n{cake}',
                           reply_markup=go_home_keyboard)
    await state.set_state(default_state)


@router.message(Text(text='Выбрать из каталога'))
async def process_select_ready_button(message: Message, state: FSMContext):
    kb_builder = InlineKeyboardBuilder()
    buttons = [InlineKeyboardButton(text=cake, callback_data=cake) for cake in ready_cakes]
    kb_builder.row(*buttons, width=3)
    await bot.send_photo(chat_id=message.chat.id, photo=ready_cakes_photo,
                         caption='Выберите ваш любимый торт',
                         reply_markup=kb_builder.as_markup())
    # await state.set_state(FSM.shape_choosing_state)


# cake = await state.get_data()
# print(cake)
# await state.clear()
# await state.set_state(default_state)


# # ветка спикера
# @router.message(Text(text='Спикер'))
# async def process_speaker_greeting(message: Message, state: FSMContext):
#     if speaker := User.objects.filter(tg_id=message.from_user.id, role='S'):
#         await message.answer(text=TEXTS['speaker_greeting'].format(speaker[0].full_name),
#                              reply_markup=next_keyboard)
#     else:
#         await message.answer(text=TEXTS['speaker_not_recognized'],
#                              reply_markup=get_id_keyboard)


# @router.message(Text(text='Узнать свой telegram id'))
# async def process_get_id(message: Message):
#     await message.answer(text=f'Ваш telegram id:\n{message.from_user.id}')


# @router.message(Text(text='Далее'))
# async def process_display_reports(message: Message):
#     text = 'Выберите доклад из списка запланированных мероприятий, чтобы начать доклад или прочитать вопросы по докладу:\n\n'
#     if reports := Report.objects.filter(speaker__tg_id=message.from_user.id, event__date=datetime.now().date()):
#         kb_builder = ReplyKeyboardBuilder()
#         for count, report in enumerate(reports, start=1):
#             text += TEXTS['reports_for_speaker'].format(count, report.event.date, report.planed_start_time, report.report_title, report.event.place)
#         buttons = [KeyboardButton(text=f'№{count} {report.report_title}') for count, report in enumerate(reports, start=1)]
#         kb_builder.row(*buttons, width=1)
#         kb_builder.row(homepage_button)
#         await message.answer(text=text, reply_markup=kb_builder.as_markup(resize_keyboard=True))
#     else:
#         await message.answer(text='У вас нет запланированных докладов на сегодня.', reply_markup=go_home_contact_organizer_keyboard)


# @router.message(lambda msg: msg.text.startswith('№'))
# async def process_report_selection(message: Message):
#     report = Report.objects.get(report_title=message.text[3:])
#     text = TEXTS['report'].format(report.report_title, report.event.date, report.planed_start_time, report.event.place)
#     btn = InlineKeyboardButton(text='Начать доклад', callback_data=report.report_title)
#     kb = InlineKeyboardMarkup(inline_keyboard=[[btn]])
#     await message.answer(text=text, reply_markup=kb)


# @router.callback_query(lambda callback: callback.data in Report.objects.all().values_list('report_title', flat=True))
# async def process_start_report(callback: CallbackQuery):
#     await callback.answer()
#     report = Report.objects.get(report_title=callback.data)
#     report.actual_start_time = datetime.now()
#     report.save()
#     btn = InlineKeyboardButton(text='Завершить доклад', callback_data='$#' + report.report_title)
#     kb = InlineKeyboardMarkup(inline_keyboard=[[btn]])
#     new_text = callback.message.text + '\n\nВы начали доклад. Когда доклад будет завершен, вы можете приступить к ответам на вопросы слушателей.'
#     await callback.message.edit_text(text=new_text, reply_markup=kb)
#     await callback.message.answer(text='Не забудьте нажать кнопку, когда закончите доклад 👆',
#                                   reply_markup=ReplyKeyboardRemove())


# @router.callback_query(lambda callback: callback.data.startswith('$#'))
# async def process_end_report(callback: CallbackQuery):
#     report = Report.objects.get(report_title=callback.data[2:])
#     report.actual_end_time = datetime.now()
#     report.save()
#     questions = Question.objects.filter(report=report)
#     text = 'Вопросы слушателей:\n'
#     for count, question in enumerate(questions, start=1):
#         text += TEXTS['question'].format(count, question.user.tg_nickname, question.question_text)
#     await callback.message.answer(text=text,
#                                   reply_markup=go_home_keyboard)


# # ветка гостя
# @router.message(Text(text='Гость мероприятия'))
# async def process_guest_greeting(message: Message, state: FSMContext):
#     await message.answer(text=TEXTS['guest_greeting'].format(message.from_user.first_name),
#                          reply_markup=guest_registration_keyboard)


# @router.message(Text(text='Ввести Email'))
# async def process_enter_email(message: Message, state: FSMContext):
#     await message.answer(text='Спасибо за доверие. Мы честно не будем спамить.\nОтправьте нам ваш Email:',
#                          reply_markup=go_home_keyboard)
#     await state.set_state(FSM.enter_email_state)


# @router.message(StateFilter(FSM.enter_email_state))
# async def enter_mail(message: Message, state: FSMContext):
#     if str(message.from_user.id) not in User.objects.all().values_list('tg_id', flat=True):
#         User.objects.update_or_create(tg_id=message.from_user.id, tg_nickname=message.from_user.username, email=message.text)
#     else:
#         user = User.objects.get(tg_id=str(message.from_user.id))
#         if not user.tg_nickname:
#             user.tg_nickname = message.from_user.username
#             user.save()
#         if not user.email:
#             user.email = message.text
#             user.save()
#     if event := Event.objects.filter(date=datetime.now().date()):
#         event = event[0]
#         await message.answer(text=TEXTS['success_registration'].format(event.event_name, event.date, event.place, event.start_time),
#                              reply_markup=event_keyboard)
#     else:
#         await message.answer(text='На сегодня нет запланированных мероприятий', reply_markup=go_home_keyboard)
#     await state.set_state(default_state)


# @router.message(Text(text=['Продолжить без Email', 'На главную']))
# async def process_without_email(message: Message, state: FSMContext):
#     if str(message.from_user.id) not in User.objects.all().values_list('tg_id', flat=True):
#         User.objects.update_or_create(tg_id=message.from_user.id, tg_nickname=message.from_user.username)
#     else:
#         user = User.objects.get(tg_id=str(message.from_user.id))
#         if not user.tg_nickname:
#             user.tg_nickname = message.from_user.username
#             user.save()
#     if event := Event.objects.filter(date=datetime.now().date()):
#         event = event[0]
#         await message.answer(text=TEXTS['success_registration'].format(event.event_name, event.date, event.place, event.start_time),
#                              reply_markup=event_keyboard)
#     else:
#         await message.answer(text='На сегодня нет запланированных мероприятий', reply_markup=go_home_keyboard)


# @router.message(Text(text='Спикеры'))
# async def process_show_speakers(message: Message, state: FSMContext):
#     event = Event.objects.filter(date=datetime.now().date())[0]
#     reports = Report.objects.filter(event=event).order_by('planed_start_time')
#     speakers = [report.speaker for report in reports]
#     kb_builder = InlineKeyboardBuilder()
#     buttons = [InlineKeyboardButton(text=speaker.full_name, callback_data=speaker.full_name) for speaker in speakers]
#     kb_builder.row(*buttons, width=1)
#     await message.answer(text=TEXTS['show_speakers'], reply_markup=kb_builder.as_markup(resize_keyboard=True))


# @router.callback_query(lambda callback: callback.data in User.objects.filter(role='S').values_list('full_name', flat=True))
# async def process_show_speaker(callback: CallbackQuery):
#     speaker = User.objects.get(full_name=callback.data)
#     await callback.answer()
#     await callback.message.answer(text=TEXTS['speaker'].format(speaker.full_name, speaker.workplace, speaker.experience))


# @router.message(Text(text='Программа мероприятия'))
# async def process_show_program(message: Message, state: FSMContext):
#     event = Event.objects.filter(date=datetime.now().date())[0]
#     reports = Report.objects.filter(event=event).order_by('planed_start_time')
#     text = f'Программа мероприятия "{event.event_name}":\nДата: {event.date}\nМесто:\n{event.place}\nДоклады:\n\n'
#     for count, report in enumerate(reports, start=1):
#         text += TEXTS['reports_for_listener'].format(count, report.planed_start_time, report.report_title, report.speaker)
#     await message.answer(text=text,
#                          reply_markup=event_homepage_keyboard)


# @router.message(Text(text='Задать вопрос спикеру'))
# async def process_ask_question(message: Message, state: FSMContext):
#     if report := Report.objects.filter(actual_start_time__isnull=False, actual_end_time__isnull=True):
#         await message.answer(text=f'Сейчас выступает: {report[0].speaker.full_name}\nТема: {report[0].report_title}\n\nЧтобы задать вопрос спикеру, который сейчас читает доклад, отправьте его текстовым сообщением:',
#                              reply_markup=event_homepage_keyboard)
#         await state.set_state(FSM.enter_question_state)
#     else:
#         await message.answer(text='На данный момент никто не выступает!',
#                              reply_markup=event_homepage_keyboard)


# @router.message(StateFilter(FSM.enter_question_state))
# async def enter_question(message: Message, state: FSMContext):
#     if report := Report.objects.filter(actual_start_time__isnull=False, actual_end_time__isnull=True):
#         Question.objects.create(question_text=message.text, user=User.objects.get(tg_id=message.from_user.id), report=report[0])
#         await message.answer(text='Спасибо за вопрос.\nСпикер ответит на него после завершения доклада.',
#                              reply_markup=event_homepage_keyboard)
#     else:
#         await message.answer(text='Извините, кажется спикер уже завершил свой доклад',
#                              reply_markup=event_homepage_keyboard)
#     await state.set_state(default_state)
