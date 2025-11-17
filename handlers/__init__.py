from aiogram import Router

from .command import command_router
from .callback import callback_router

main_router = Router()

main_router.include_routers(
    callback_router,
    command_router,
)
