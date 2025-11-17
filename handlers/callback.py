from aiogram import Router, Bot, F
from aiogram.types import CallbackQuery

import config
from google_api import client as google_client
from keyboards import ikb_users_answers, ikb_newlyweds_answers
from keyboards.callback_data import CallbackAnswers

callback_router = Router()


@callback_router.callback_query(CallbackAnswers.filter(F.button == 'back'))
async def main_menu(callback: CallbackQuery, bot: Bot):
    users = google_client.get_answers()
    if users:
        msg_text = f'Привет, {callback.from_user.full_name}!\nВот ссылка на тест:\n{config.TEST_URL}'
        keyboard = ikb_users_answers(users)
    else:
        msg_text = 'Ответов нет!'
        keyboard = None
    await bot.edit_message_text(
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
        text=msg_text,
        reply_markup=keyboard,
    )


@callback_router.callback_query(CallbackAnswers.filter(F.button == 'delete'))
async def delete_answers(callback: CallbackQuery, callback_data: CallbackAnswers, bot: Bot):
    google_client.delete_answers(callback_data.idx)
    await callback.answer(
        text='Ответы удалены',
        show_alert=True,
    )
    await main_menu(callback, bot)


@callback_router.callback_query(CallbackAnswers.filter(F.button == 'answers'))
async def newlyweds_answers(callback: CallbackQuery, callback_data: CallbackAnswers, bot: Bot):
    answers = google_client.get_answers()
    newlyweds = answers[callback_data.idx]
    await bot.edit_message_text(
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
        text=newlyweds.str_answers(),
        reply_markup=ikb_newlyweds_answers(callback_data.idx),
    )
