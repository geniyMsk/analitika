# -*- coding: utf-8 -*-
import logging
import datetime
from aiogram import Dispatcher
from aiogram.types import ParseMode, BotCommand, BotCommandScope, BotCommandScopeChat

from config import ADMINS
from loader import bot

import dir.DBCommands as db
import dir.keyboard as kb


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            pass
        except Exception as err:
            logging.error(err)

