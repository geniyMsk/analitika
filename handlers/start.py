# -*- coding: utf-8 -*-
import datetime
import logging

import aiogram.types
from aiogram.dispatcher import filters

from loader import bot, dp
from config import ADMINS
from aiogram import types
from aiogram.types import Message, CallbackQuery, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, \
    InlineQueryResultArticle, InputMessageContent
import dir.DBCommands as db
import dir.states as states
from dir.keyboard import keyboards

kb = keyboards()


@dp.message_handler(commands='start', state='*')
async def start(message: Message):
    db.create_tables()
    chat_ids = db.get_all_chat_id()
    chat_id = message.from_user.id

    if (chat_id,) not in chat_ids:
        username = message.from_user.username
        db.add_user(chat_id, username)
    await message.answer('''Привет.
Чтоб бы начать зарабатывать от 60.000 тебе нужно сделать два простых действия
1. Пройти тест (бесплатно)
2. Пройти бесплатное обучение по скайпу 
Это подойдёт даже для тех кто в этом не разбирается❗️
После тебе откроются доступы к аналитике и ты начнёшь зарабатывать
Все что тебе потребуется — это пару часов в день и компьютер''', reply_markup=kb.ready)
    await states.state.READY.set()


@dp.message_handler(state=states.state.READY, text='Я готов')
async def ready(message: Message):
    await message.answer('Какой спорт предпочитаешь?', reply_markup=kb.sport)
    await states.state.SPORT.set()


@dp.message_handler(state=states.state.SPORT)
async def sport(message: Message):
    await message.answer(text='''Чтобы получить доступ к полному обучению оплати 299₽ 
на карту Сбербанка
4817 7602 4486 4520
(Глеб Владимирович)
Отправь скрин об оплате нашему менеджеру @AnalitikaSportMatcei
И сразу получи доступ к ссылке 
Проходи обучение и начинай зарабатывать 💰''', reply_markup=aiogram.types.ReplyKeyboardRemove())
    db.set_date_last_message(chat_id=message.chat.id)
