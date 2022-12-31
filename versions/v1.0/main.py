# импорт библиотек
from aiogram import Bot, Dispatcher, executor, types
import asyncio
import api_id as ai
import text as txt
import db as db
import time
import random
import logging

# персональные настройки (для /admin)
autodelete = 180
quickdelete = 60
spamdelete = 30

# Авторизация бота
logging.basicConfig(level=logging.INFO)
bot = Bot(token=ai.API_TOKEN)
dp = Dispatcher(bot)

# Приветствие при новом пользователе ДОДЕЛАТЬ!!!
@dp.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    user_name = message.new_chat_member.first_name
    bot.send_message(message.chat.id, "Добро пожаловать, {0}!".format(user_name))

# Игнор лс СДЕЛАТЬ!!!
#@dp.message_handler(...)
#   async def NewUser():

# рандомная рассылка СДЕЛАТЬ!!!
#@dp.message.hendler()

# /menu
@dp.message_handler(commands=['menu'])
async def scammenu(message: types.Message):
    bot_logo = open('logo.jpg', 'rb')
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text=txt.scamhelp_button_text, callback_data='callback_scamhelp'))
    keyboard.add(types.InlineKeyboardButton(text=txt.scam_button_text, callback_data='callback_scam'))
#   keyboard.add(types.InlineKeyboardButton(text=txt.scam2_button_text, callback_data='callback_scam2'))
#   keyboard.add(types.InlineKeyboardButton(text=txt.scamversions_button_text, callback_data='callback_versions'))
    keyboard.add(types.InlineKeyboardButton(text=txt.account_button_text, callback_data='callback_account'))
    keyboard.add(types.InlineKeyboardButton(text=txt.scamdonate_button_text, url=txt.scamdonate_link))
    keyboard.add(types.InlineKeyboardButton(text=txt.language_button_text, callback_data='callback_language'))
    rus = types.InlineKeyboardButton(text='🇷🇺', callback_data='callback_russian')
    eng = types.InlineKeyboardButton(text='🇺🇸', callback_data='callback_english')
    ukr = types.InlineKeyboardButton(text='🇺🇦', callback_data='callback_ukrain')
    keyboard.row(rus, ukr, eng)
    delete = await message.reply_photo(bot_logo, txt.scammenu_start, reply_markup = keyboard)
    await asyncio.sleep(autodelete)
    await message.delete()
    await delete.delete()

# scamhelp callback
@dp.callback_query_handler(text="callback_scamhelp")
async def CallbackScamHelp(message: types.Message):
    await message.answer(txt.alert_text)
    await bot.send_message(message.from_user.id,txt.scamhelp_text)
    delete = await bot.send_message(ai.CHAT_ID, txt.direct_text)
    await asyncio.sleep(quickdelete)
    await delete.delete()
    await message.delete()

# callback versions
@dp.callback_query_handler(text="callback_scam")
async def CallbackVersions(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text=txt.archive_button_text, url=txt.archive_button_link))
    delete = await bot.send_message(ai.CHAT_ID, txt.archive_text, reply_markup = keyboard)
    await asyncio.sleep(quickdelete)
    await delete.delete()
    await message.delete()

# account callback
@dp.callback_query_handler(text="callback_account")
async def CallbackScamAccount(message: types.Message):
    await message.answer(txt.future_text)

# language callback
@dp.callback_query_handler(text="callback_language")
async def CallbackLanguage(message: types.Message):
    await message.answer(txt.language_text)

# /donate
@dp.message_handler(commands=['donate'])
async def scamdonate(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text=txt.scamdonate_button_text, url=txt.scamdonate_link))
    await message.reply(txt.scamdonate_text, reply_markup = keyboard)

# /admin СДЕЛАТЬ!!!
@dp.message_handler(commands=['admin'])
async def admin(message: types.Message):
    delete = await message.reply(txt.admin_error)
    await asyncio.sleep(autodelete)
    await delete.delete()
    await message.delete()

# /account ДОДЕЛАТЬ!!!
@dp.message_handler(commands=['account'])
async def admin(message: types.Message):
    delete = await message.reply(txt.error_text)
    await asyncio.sleep(autodelete)
    await delete.delete()
    await message.delete()

# /help 
@dp.message_handler(commands=['help'])
async def admin(message: types.Message):
    delete = await bot.send_message(ai.CHAT_ID, txt.help_text)
    await asyncio.sleep(quickdelete)
    await delete.delete()
    await message.delete()

# логирование СДЕЛАТЬ!!!

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)