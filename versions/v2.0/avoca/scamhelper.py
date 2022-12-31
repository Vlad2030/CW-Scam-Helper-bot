# bot.py
# автоустановка библиотек, если отсуствует
try:
    from loguru import logger
    logger.add("logs.log", enqueue=False, backtrace=False, catch=False)
    logger.info("imported loguru")
    logger.info("importing modules...")
    from aiogram import Bot, Dispatcher, executor, types

    logger.info("aiogram imported Bot, Dispatcher, executor, types")
    # импорт стейтов
    from aiogram.contrib.fsm_storage.memory import MemoryStorage

    logger.info("aiogram.contrib.fsm_storage.memory imported MemoryStorage")
    from aiogram.dispatcher import FSMContext

    logger.info("aiogram.dispatcher imported FSMContext")
    from aiogram.dispatcher.filters.state import State, StatesGroup

    logger.info("aiogram.dispatcher.filters.state imported State, StatesGroup")
    from aiogram.utils.exceptions import MessageNotModified

    logger.info("aiogram.utils.exceptions imported MessageNotModified")
    import os

    logger.info("imported os")
    import sys

    logger.info("imported sys")
    import requests

    logger.info("imported requests")
    import asyncio

    logger.info("imported asyncio")
    import sqlite3

    logger.info("imported sqlite3")
    import json

    logger.info("imported json")
    import colorama

    logger.info("imported colorama")
except ImportError:
    logger.error("ImportError: trying install...")
    os.system("pip install -r requirements.txt")
finally:
    logger.success("all modules imported successfully!\n")


try:
    logger.info("importing root main")
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    sys.path.append(root)
    import main
except:
    logger.error("import root fail!\n")
finally:
    logger.success("import root successfull\n")


try:
    logger.info("importing bot/modules/*.py")
    # импорт .py кода из .../bot/modules/
    from .modules import api_token

    logger.info("from bot/modules/api_token.py imported")
    from .modules import id

    logger.info("from bot/modules/id.py imported")
    from .modules import keyboard

    logger.info("from bot/modules/keyboard.py imported")
    from .modules import text

    logger.info("from bot/modules/text.py imported")
except:
    logger.error("import bot/modules/*.py modules fail!\n")
finally:
    logger.success("import bot/modules/*.py modules successfull\n")


betatest = "0"
# sys.setrecursionlimit(10000)


# авторизация бота
bot = Bot(
    token=api_token.TOKEN,
    parse_mode=types.ParseMode.HTML
)
storage = MemoryStorage()
dp = Dispatcher(
    bot,
    storage=storage
)


async def GetOnline():
    return online


@dp.chat_join_request_handler()
async def join_request(update: types.ChatJoinRequest):
    user_id = await update.from_user.id
    await bot.send_message(user_id, text.requestad_text)
    # можно добавить пользователя в бд для дальнейших рассылок
    return None


# /menu
@dp.message_handler(commands=['menu', 'start'])
async def Menu(message: types.Message):
    logger.info("/menu from {user_id} id", user_id=message.from_user.id)
    await message.reply(
        text=text.menu_text,
        reply_markup=keyboard.MenuKeyboard()
    )
    return None


@dp.callback_query_handler(text="get_instruction")
async def GetInstruction(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.instruction_text,
        reply_markup=keyboard.ReturnKeyboard(),
    )
    return None


@dp.callback_query_handler(text="get_scam")
async def GetScam(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.getscam_text,
        reply_markup=keyboard.CWSCAMKeyboard(),
    )
    return None


@dp.callback_query_handler(text="get_online")
async def GetOnline(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.answer_callback_query(
        callback_query.id,
        text=text.error_text,
        show_alert=False,
        reply_markup=keyboard.ReturnKeyboard(),
    )
    return None


@dp.callback_query_handler(text="get_private")
async def GetPrivate(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.answer_callback_query(
        callback_query.id,
        text=text.private_text,
        reply_markup=keyboard.BuyPrivateKeyboard(),
    )
    return None


@dp.callback_query_handler(text="get_beta")
async def GetBeta(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    if betatest == "1":
        logger.warning("betatest==True")
    elif betatest == "0":
        logger.warning("betatest==False")
        await bot.answer_callback_query(
            callback_query.id, text=text.betausererror_text, show_alert=True
        )
        await bot.answer_callback_query(
            callback_query.id,
            text=text.betausererror_text,
            show_alert=False,
            reply_markup=keyboard.ReturnKeyboard(),
        )
    return None


@dp.callback_query_handler(text="donate")
async def Donate(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.donate_text,
        reply_markup=keyboard.DonateKeyboard(),
    )
    return None


@dp.callback_query_handler(text="return")
async def Return(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.menu_text,
        reply_markup=keyboard.MenuKeyboard(),
    )
    return None


@dp.callback_query_handler(text="rus")
async def Russian(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.menu_text,
        reply_markup=keyboard.MenuKeyboard(),
    )
    return None


@dp.callback_query_handler(text="eng")
async def English(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.menu_text,
        reply_markup=keyboard.MenuKeyboard(),
    )
    return None


# бесполезная хрень, но удалять страшно
@dp.errors_handler(exception=MessageNotModified)
async def message_not_modified_handler(update, error):
    return True
