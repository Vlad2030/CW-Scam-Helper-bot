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
    import random
    logger.info("imported random")
    import time
    logger.info("imported time")
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
    root = os.path.abspath(
        os.path.join(
            os.path.dirname(
                __file__
            ),
            os.pardir
        )
    )
    sys.path.append(root)
    import main
except:
    logger.error("import root fail!\n")
finally:
    logger.success("import root successfull\n")




logger.info("importing bot/modules/*.py")
# импорт .py кода из .../bot/modules/
from .modules import api_token
logger.info("from bot/modules/api_token.py imported")
from .modules import id
logger.info("from bot/modules/id.py imported")
from .modules import keyboard
logger.info("from bot/modules/keyboard.py imported")
from .modules import text
logger.info("from bot/modules/text.py imported\n")
from .modules import online
logger.info("from bot/modules/online.py imported\n")


betatest = "0"
# sys.setrecursionlimit(10000)



# подключение к базе данных
try:
    database = sqlite3.connect(
        'avoca/database/database.db'
    )
    logger.success(
        'sqlite database/database.db connected!'
    )
except sqlite3.Error as error:
    logger.error(
        'sqlite error ({errordb}).',
        errordb=error
    )


try:
    database2 = sqlite3.connect(
        'avoca/database/requests.db'
    )
    logger.success(
        'sqlite database/requests.db  connected!\n'
    )
except sqlite3.Error as error:
    logger.error(
        'sqlite error ({errordb}).\n',
        errordb=error
    )



# авторизация бота
bot = Bot(token=api_token.TOKEN,
    parse_mode=types.ParseMode.HTML
)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)



logger.add("actions.log", enqueue=False, backtrace=False, catch=False)



@dp.chat_join_request_handler()
async def join_request(update: types.ChatJoinRequest):
    await update.approve()
    await bot.send_message(
        chat_id=update.from_user.id,
        text=text.ru_text.requestad_text,
    )
    cur = database2.cursor()
    cur.execute(
        f'''INSERT INTO users VALUES (NULL, "{message.from_user.id}")'''
    )
    database2.commit()
    return None



# /menu
@dp.message_handler(commands=['menu', 'start'])
async def Menu(message: types.Message):
    logger.info(
        "/menu from {user_id} id",
        user_id=message.from_user.id
    )
    cur = database.cursor()
    cur.execute(
        f'SELECT * FROM users WHERE user_id = {message.chat.id}'
    )
    result = cur.fetchone()
    if result is None:
            cur = database.cursor()
            cur.execute(
                f'''SELECT * FROM users WHERE (user_id="{message.from_user.id}")'''
            )
            entry = cur.fetchone()
            if entry is None:
                cur.execute(
                    f'''INSERT INTO users VALUES (NULL, "{message.from_user.id}")'''
                )
                database.commit()
    await message.reply(
        text=text.ru_text.menu_text,
        reply_markup=keyboard.ru_keyboard.ruMenuKeyboard()
    )
    return None



@dp.message_handler(commands='online')
async def getOnline(message: types.Message):
    logger.info(
        "/online from {user_id} id",
        user_id=message.from_user.id
    )
    await message.reply(text=online.sendRequest())
    return None


# RU ##############################################################
@dp.callback_query_handler(text="ru_get_instruction")
async def ruGetInstruction(callback_query: types.CallbackQuery):
    logger.info(
        "callback get_instruction from {user_id} id",
        user_id=callback_query.from_user.id
    )
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.ru_text.instruction_text,
        reply_markup=keyboard.ru_keyboard.ruReturnKeyboard()
    )
    return None


@dp.callback_query_handler(text="ru_get_scam")
async def ruGetScam(callback_query: types.CallbackQuery):
    logger.info(
        "callback get_scam from {user_id} id",
        user_id=callback_query.from_user.id
    )
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.ru_text.getscam_text,
        reply_markup=keyboard.ru_keyboard.ruCWSCAMKeyboard()
    )
    return None


@dp.callback_query_handler(text="ru_get_online")
async def ruGetOnline(callback_query: types.CallbackQuery):
    logger.info(
        "callback get_online from {user_id} id",
        user_id=callback_query.from_user.id
    )
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=online.sendRequest(),
        reply_markup=keyboard.ru_keyboard.ruReturnKeyboard()
    )
    return None


@dp.callback_query_handler(text="ru_get_private")
async def ruGetPrivate(callback_query: types.CallbackQuery):
    logger.info(
        "callback get_private from {user_id} id",
        user_id=callback_query.from_user.id
    )
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.ru_text.private_text,
        reply_markup=keyboard.ru_keyboard.ruBuyPrivateKeyboard()
    )
    return None


@dp.callback_query_handler(text="ru_get_beta")
async def ruGetBeta(callback_query: types.CallbackQuery):
    logger.info(
        "callback get_beta from {user_id} id",
        user_id=callback_query.from_user.id
    )
    await bot.answer_callback_query(callback_query.id)
    if betatest == "1":
        logger.warning("betatest==True")
    elif betatest == "0":
        logger.warning("betatest==False")
        await callback_query.bot.edit_message_text(
            message_id=callback_query.message.message_id,
            chat_id=callback_query.message.chat.id,
            text=text.ru_text.betausererror_text,
            reply_markup=keyboard.ru_keyboard.ruReturnKeyboard()
        )
    return None


@dp.callback_query_handler(text="ru_donate")
async def ruDonate(callback_query: types.CallbackQuery):
    logger.info(
        "callback donate from {user_id} id",
        user_id=callback_query.from_user.id
    )
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.ru_text.donate_text,
        reply_markup=keyboard.ru_keyboard.ruDonateKeyboard()
    )
    return None


@dp.callback_query_handler(text="ru_return")
async def ruReturn(callback_query: types.CallbackQuery):
    logger.info(
        "callback return from {user_id} id",
        user_id=callback_query.from_user.id
    )
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.ru_text.menu_text,
        reply_markup=keyboard.ru_keyboard.ruMenuKeyboard()
    )
    return None
#################################################################


# EN ############################################################
@dp.callback_query_handler(text="en_get_instruction")
async def enGetInstruction(callback_query: types.CallbackQuery):
    logger.info(
        "callback get_instruction from {user_id} id",
        user_id=callback_query.from_user.id
    )
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.en_text.instruction_text,
        reply_markup=keyboard.en_keyboard.enReturnKeyboard()
    )
    return None


@dp.callback_query_handler(text="en_get_scam")
async def enGetScam(callback_query: types.CallbackQuery):
    logger.info(
        "callback get_scam from {user_id} id",
        user_id=callback_query.from_user.id
    )
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.en_text.getscam_text,
        reply_markup=keyboard.en_keyboard.enCWSCAMKeyboard()
    )
    return None


@dp.callback_query_handler(text="en_get_online")
async def enGetOnline(callback_query: types.CallbackQuery):
    logger.info(
        "callback get_online from {user_id} id",
        user_id=callback_query.from_user.id
    )
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=online.sendRequest(),
        reply_markup=keyboard.en_keyboard.enReturnKeyboard()
    )
    return None


@dp.callback_query_handler(text="en_get_private")
async def enGetPrivate(callback_query: types.CallbackQuery):
    logger.info(
        "callback get_private from {user_id} id",
        user_id=callback_query.from_user.id
    )
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.en_text.private_text,
        reply_markup=keyboard.en_keyboard.enBuyPrivateKeyboard()
    )
    return None


@dp.callback_query_handler(text="en_get_beta")
async def enGetBeta(callback_query: types.CallbackQuery):
    logger.info(
        "callback get_beta from {user_id} id",
        user_id=callback_query.from_user.id
    )
    await bot.answer_callback_query(callback_query.id)
    if betatest == "1":
        logger.warning("betatest==True")
    elif betatest == "0":
        logger.warning("betatest==False")
        await callback_query.bot.edit_message_text(
            message_id=callback_query.message.message_id,
            chat_id=callback_query.message.chat.id,
            text=text.en_text.betausererror_text,
            reply_markup=keyboard.en_keyboard.enReturnKeyboard()
        )
    return None


@dp.callback_query_handler(text="en_donate")
async def enDonate(callback_query: types.CallbackQuery):
    logger.info(
        "callback donate from {user_id} id",
        user_id=callback_query.from_user.id
    )
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.en_text.donate_text,
        reply_markup=keyboard.en_keyboard.enDonateKeyboard()
    )
    return None


@dp.callback_query_handler(text="en_return")
async def enReturn(callback_query: types.CallbackQuery):
    logger.info(
        "callback return from {user_id} id",
        user_id=callback_query.from_user.id
    )
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.en_text.menu_text,
        reply_markup=keyboard.en_keyboard.enMenuKeyboard()
    )
    return None


@dp.message_handler(commands=['ad'])
async def Advertise(message: types.Message):
    args = message.get_args().split()
    if args==['1']:
        logger.info(
            "ad turned on"
        )
        await bot.send_message(
            chat_id='-1001707312411',
            text=text.ru_text.ad_text,
            reply_markup=keyboard.DonateADKeyboard()
        )
        cooldown = random.randint(1000, 10000)
        cooldown_min = cooldown / 60
        logger.info(
            "ad sent! next after {cooldown_time} minutes",
            cooldown_time=cooldown_min
        )
    if args==['0']:
        logger.info(
            "ad turned off"
        )
    return None
###########################################################


@dp.callback_query_handler(text="rus")
async def Russian(callback_query: types.CallbackQuery):
    logger.info(
        "callback rus from {user_id} id",
        user_id=callback_query.from_user.id
    )
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.ru_text.menu_text,
        reply_markup=keyboard.ru_keyboard.ruMenuKeyboard()
    )
    return None


@dp.callback_query_handler(text="eng")
async def English(callback_query: types.CallbackQuery):
    logger.info(
        "callback eng from {user_id} id",
        user_id=callback_query.from_user.id
    )
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.en_text.menu_text,
        reply_markup=keyboard.en_keyboard.enMenuKeyboard()
    )
    return None


# админ панель ########################################################
@dp.message_handler(commands='admin')
async def adminPanel(message: types.Message):
    if message.from_user.id==id.ADMIN_ID:
        await message.reply(
            text=text.admin_text.admin_menu_text,
            reply_markup=keyboard.admin_keyboard.adminMenuKeyboard()
        )
    else:
        await message.reply(text=text.admin_text.not_admin_text)
    return None


@dp.callback_query_handler(text="admin_menu")
async def adminPanelReturn(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.admin_text.admin_menu_text,
        reply_markup=keyboard.admin_keyboard.adminMenuKeyboard()
    )
    return None


@dp.callback_query_handler(text="say_via_bot")
async def adminSayViaBot(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.admin_text.say_via_bot_text,
        reply_markup=keyboard.admin_keyboard.adminMenuReturnKeyboard()
    )
    # TODO: Доделать
    return None


@dp.callback_query_handler(text="ban_user")
async def adminBanUser(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.admin_text.penalty_user_text,
        reply_markup=keyboard.admin_keyboard.adminMenuReturnKeyboard()
    )
    # TODO: Доделать
    return None


@dp.callback_query_handler(text="mute_user")
async def adminMuteUser(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.admin_text.penalty_user_text,
        reply_markup=keyboard.admin_keyboard.adminMenuReturnKeyboard()
    )
    return None


@dp.callback_query_handler(text="fuckoff_user")
async def adminFuckOffUser(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.admin_text.penalty_user_text,
        reply_markup=keyboard.admin_keyboard.adminMenuReturnKeyboard()
    )
    return None


@dp.callback_query_handler(text="moders")
async def adminModers(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.admin_text.moders_menu_text,
        reply_markup=keyboard.admin_keyboard.adminModersMenuKeyboard()
    )
    return None


'''@dp.callback_query_handler(text="statistics")
async def adminStatistics(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=,
        reply_markup=keyboard.admin_keyboard.adminPanelReturn()
    )
    return None'''



'''@dp.callback_query_handler(text="")
async def (callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.admin_text.,
        reply_markup=keyboard.admin_keyboard.()
    )
    return None


@dp.callback_query_handler(text="")
async def (callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.admin_text.,
        reply_markup=keyboard.admin_keyboard.()
    )
    return None


@dp.callback_query_handler(text="")
async def (callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.admin_text.,
        reply_markup=keyboard.admin_keyboard.()
    )
    return None



@dp.callback_query_handler(text="")
async def (callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.bot.edit_message_text(
        message_id=callback_query.message.message_id,
        chat_id=callback_query.message.chat.id,
        text=text.admin_text.,
        reply_markup=keyboard.admin_keyboard.()
    )
    return None'''
#######################################################################


# бесполезная херь, но удалять страшно
@dp.errors_handler(exception=MessageNotModified)
async def message_not_modified_handler(update, error):
    return True
