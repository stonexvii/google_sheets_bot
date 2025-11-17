from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

import config
from google_api import client as google_client
from keyboards import ikb_users_answers

command_router = Router()


@command_router.message(Command('start'))
async def command_start(message: Message):
    users = google_client.get_answers()
    if users:
        msg_text = f'Привет, {message.from_user.id}!\nВот ссылка на тест: {config.TEST_URL}'
        keyboard = ikb_users_answers(users)
    else:
        msg_text = 'Ответов нет!'
        keyboard = None
    await message.answer(
        text=msg_text,
        disable_web_page_preview=True,
        reply_markup=keyboard,
    )
