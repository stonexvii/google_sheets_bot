from aiogram.utils.keyboard import InlineKeyboardBuilder

from classes import UserAnswers
from .buttons import KeyboardButton
from .callback_data import CallbackAnswers


def ikb_users_answers(answers: list[UserAnswers]):
    keyboard = InlineKeyboardBuilder()
    for idx, answer in enumerate(answers):
        keyboard.button(**KeyboardButton(answer.button(), CallbackAnswers, button='answers', idx=idx).as_kwargs())
    keyboard.adjust(1)
    return keyboard.as_markup()


def ikb_newlyweds_answers(idx: int):
    keyboard = InlineKeyboardBuilder()
    keyboard.button(**KeyboardButton('Удалить', CallbackAnswers, button='delete', idx=idx).as_kwargs())
    keyboard.button(**KeyboardButton('Назад', CallbackAnswers, button='back').as_kwargs())
    return keyboard.as_markup()
