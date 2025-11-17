from aiogram.filters.callback_data import CallbackData


class CallbackAnswers(CallbackData, prefix='CA'):
    button: str
    idx: int = 0
