# -*- coding: utf-8 -*-
import datetime
import logging

from aiogram.dispatcher import filters

from loader import bot, dp
from config import ADMINS
from aiogram import types
from aiogram.types import Message, CallbackQuery, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, \
    InlineQueryResultArticle, InputMessageContent, BotCommand, BotCommandScopeChat
import dir.DBCommands as db
import dir.states as states
from dir.keyboard import keyboards


@dp.message_handler(commands=['stat'], state='*')
async def stat(message: Message):
    if message.from_user.username in ADMINS:
        all_reg = db.count_all_reg()
        today_reg = db.count_all_reg_today()
        last_all = db.count_last_message()
        last_today = db.count_last_message_today()

        try:
            await bot.set_my_commands(commands=[BotCommand(command='stat', description='Статистика')],
                                  scope=BotCommandScopeChat(chat_id=message.chat.id))
            await message.answer(f'Статистика:\n'
                                 f'общее кол-во /start-вших: {all_reg}\n'
                                 f'общее кол-во дошедших до финального сообщения: {today_reg}\n'
                                 f'за сегодня  кол-во /start-вших: {last_all}\n'
                                 f'за сегодня кол-во дошедших до финального сообщения: {last_today}')
        except:
            pass
@dp.message_handler(commands='logging', state='*')
async def send_logs(message: Message):
    if message.from_user.username in ADMINS:
        await bot.send_chat_action(message.chat.id, 'upload')
        await message.answer_document(open(r'logs.log', 'rb'))
