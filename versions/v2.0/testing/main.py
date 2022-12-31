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



class ApiToken:
    # ID бота из t.me/BotFather
    TOKEN = 'token'



class Texts():
    # текст сообщений
    menu_text = "Добро пожаловать в меню бота 👋"
    instruction_text = """
    Полная инструкция где скачать, установить и пользоваться SCAM mode

    <b>УСТАНОВКА:</b>
      1. Скачиваем SCAM mode (ниже прикреплён файл с актуальной версией SCAM mode).
      2. Распаковываем где вам удобно.
      3. Находим папку с игрой и кидаем файл Assembly-CSharp.dll по адресу <code>CWClient\CWclient_Data\Managed</code> с заменой (перед этим надо закрыть игру).

    <b>ИСПОЛЬЗОВАНИЕ:</b>
      после того как успешно зашли в игру заходить в консоль (клавиша ~) и вводим scam (активирует SCAM mode).
      все камуфляжи на любое оружие и обвесы активированы сразу, можно даже не писать scam.
    Теперь пройдемся по командам:
      <code>scam</code> - включение SCAM Mode
      <code>scam_off</code> - отключение SCAM Mode
      <code>scam_hc</code> - перенос интерфейса аркадного режима в хардкор + умения, теплак и прочее..
      <code>proscam</code> - активирует команды scam_hc, devmode, freegun, full_thermal
      <code>freegun</code> - свободный выбор оружия во время боя
      <code>devmode</code> - активирует аим (зажать клавишу N) и вх
      <code>addnickchanges 10</code> - добавляет 10 (можно любое число вписать) смен ника
      <code>wtask ID</code> - покупка wtaskов (надо указать ID оружия и также накрутить GP)
      <code>GP 1000</code> - накрутка GP (визуал)
      <code>SP 100</code> - накрутка SP (визуал)
      <code>CR 100000</code> - накрутка CR (визуал)
      <code>level 71</code> - делает вас 71 lvl (визуал)
      <code>repa 500</code> - поставить 500 репутации (визуал)
      <code>exp 500</code> - поставить 500 опыта (визуал)
      <code>wipewtask</code> - снять все wtask (визуал)
      <code>masterofarms</code> - поставить все wtask (визуал)
      <code>knifedelay</code> - быстрый нож
      <code>buyanov</code> - глаз буянова - 100% точность (визуал)
      <code>hidden_server_access</code> - отображение скрытых игроков и прочее..
      <code>addsnow</code> - добавляет снег на карту
      <code>full_thermal</code> - тепловизор на всю карту (или клавиша b в proscam/devmode)
      <code>show_enemy_nick</code> - отображение ников при засвете или попадании в игроков
      <code>connect_over_limit</code> - возможность заходить на карты при полном заполнении
      <code>clear</code> - очищает консоль
      <code>showcross</code> - перекрёстный crosshair
      <code>s_debug</code> - список серверов
      <code>targetframerate 144</code> - ограничение FPS до нужного вам числа
      <code>list</code> - показывает список игроков на сервере
      <code>online</code> - показывает количество игроков в игре
      <code>socialID</code> - ваш ID в социальной сети
      <code>userID</code> - ваш ID в игре
      <code>weapinfo</code> - информация об оружии (только на сервере)
      <code>promo (XXXXX-XXXXX-XXXXX-XXXXX-XXXXX)</code> - активация промокода
      <code>clearprofile</code> - сбросить профиль (НЕ визуал)
      <code>Fixed delta time -1</code> - фиксированный интервал
      <code>http_debug</code> - откладка http-запросов

    Все команды написаны в настройках во вкладке <b>SCAM info</b>
    """
    needsubscribe_text = "Для получения нужно подписаться на определенные каналы"
    betausererror_text = "❌В данное время не проводятся бета-тесты, приходите позже"
    error_text = "⛔Временно не доступно!"
    donate_text = "Выберите вид пожертвования:"
    getscam_text = "Получить SCAM mode можно в данном канале ↓"
    requestad_text = """<b>Мы рады что ты присоединился в наше сообщество КВшеров!\n</b>
    Предлагаем все тебе все наши каналы:
    <a href="">Avoca<a/> - наш чат
    <a href="">CW SCAM<a/> - канал SCAM mode
    <a href="">CW MARKET<a/> - биржа аккаунтов Contract Wars

    А также ты можешь пожертвовать немного:
    <a href="https://www.donationalerts.com/r/avoca">Разработчику<a/>
    <a href="https://www.qiwi.com/n/VLAD2030">На работу бота<a/>
    """


    privat_price = 500
    private_text = "Что-бы получить доступ к закрытому сообществу и знать информацию, а также ранние билды раньше всех, нужно купить доступ за <b>{privat_price}₽</b> по кнопке ниже и отписать @avoca_cw"


    # текст кнопок
    instruction_buttontext = "📝Инструкция"
    yourad_buttontext = "🎫Здесь могла бы быть ваша реклама"
    getSCAM_buttontext = "📄Получить SCAM"
    getonline_buttontext = "🌐Текущий онлайн"
    private_buttontext = "🔒Приватный канал"
    betauser_buttontext = "🆕Стать бета-тестером"
    cwmarket_buttontext = "📈Биржа аккаунтов"
    donate_buttontext = "💸Помочь проекту"
    avoca_buttontext = "Задонатить создателю мода"
    server_buttontext = "Задонатить на поддержку бота"
    russian_buttontext = "🇷🇺"
    english_buttontext = "🇺🇸"
    CWSCAM_buttontext = "CW SCAM"
    buy_buttontext = 'Купить'
    back_buttontext = "↩Назад"



class Keyboards:
    def MenuKeyboard():
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            types.InlineKeyboardButton(
                text=Texts().instruction_buttontext,
                callback_data="get_instruction"
            ),
            types.InlineKeyboardButton(
                text=Texts().getSCAM_buttontext,
                callback_data="get_scam"
            ),
            types.InlineKeyboardButton(
                text=Texts().getonline_buttontext,
                callback_data="get_online"
            ),
            types.InlineKeyboardButton(
                text=Texts().private_buttontext,
                callback_data="get_private"
            ),
            types.InlineKeyboardButton(
                text=Texts().betauser_buttontext,
                callback_data="get_beta"
            ),
            types.InlineKeyboardButton(
                text=Texts().cwmarket_buttontext,
                url="https://t.me/CWMarketShop"
            ),
            types.InlineKeyboardButton(
                text=Texts().donate_buttontext,
                callback_data="donate"
            )
        )
        keyboard.add(
            types.InlineKeyboardButton(
                text=Texts().russian_buttontext,
                callback_data="rus"
            ),
            types.InlineKeyboardButton(
                text=Texts().english_buttontext,
                callback_data="eng"
            )
        )
        logger.info('')
        return keyboard


    def ReturnKeyboard():
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            types.InlineKeyboardButton(
                text=Texts().return_buttontext,
                callback_data="menu"
            )
        )
        return keyboard


    def DonateKeyboard():
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            types.InlineKeyboardButton(
                text=Texts().avoca_buttontext,
                url="https://www.donationalerts.com/r/avoca"
            )
        )
        keyboard.add(
            types.InlineKeyboardButton(
                text=Texts().server_buttontext,
                url="https://www.qiwi.com/n/VLAD2030"
            )
        )
        keyboard.add(
            types.InlineKeyboardButton(
                text=Texts().return_buttontext,
                callback_data="menu"
            )
        )
        return keyboard


    def CWSCAMKeyboard():
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            types.InlineKeyboardButton(
                text=Texts().CWSCAM_buttontext,
                url="https://t.me/+s2wTdUM95eMzMDQy"
            )
        )
        keyboard.add(
            types.InlineKeyboardButton(
                text=Texts().return_buttontext,
                callback_data="menu"
            )
        )
        return keyboard


    def BuyPrivateKeyboard():
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            types.InlineKeyboardButton(
                text=Texts().buy_buttontext,
                url="https://www.donationalerts.com/r/avoca"
            )
        )
        return keyboard



class Avoca:

    betatest = "0"
    # sys.setrecursionlimit(10000)

    # авторизация бота
    bot = Bot(
        token=ApiToken.TOKEN,
        parse_mode=types.ParseMode.HTML
    )
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)



    async def GetOnline():
        return online



    @dp.chat_join_request_handler()
    async def join_request(update: types.ChatJoinRequest):
        user_id = await update.from_user.id
        await bot.send_message(user_id, Texts().requestad_text)
        # можно добавить пользователя в бд для дальнейших рассылок
        return None



    # /menu
    @dp.message_handler(commands=['menu', 'start'])
    async def Menu(message: types.Message):
        logger.info("/menu from {user_id} id", user_id=message.from_user.id)
        await message.reply(
            text=Texts().menu_text,
            reply_markup=Keyboards.MenuKeyboard()
        )
        return None


    @dp.callback_query_handler(text="get_instruction")
    async def GetInstruction(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        await callback_query.bot.edit_message_text(
            message_id=callback_query.message.message_id,
            chat_id=callback_query.message.chat.id,
            text=Texts().instruction_text,
            reply_markup=Keyboards.ReturnKeyboard(),
        )
        return None


    @dp.callback_query_handler(text="get_scam")
    async def GetScam(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        await callback_query.bot.edit_message_text(
            message_id=callback_query.message.message_id,
            chat_id=callback_query.message.chat.id,
            text=Texts().getscam_text,
            reply_markup=Keyboards.CWSCAMKeyboard(),
        )
        return None


    @dp.callback_query_handler(text="get_online")
    async def GetOnline(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        await bot.answer_callback_query(
            callback_query.id,
            text=Texts().error_text,
            show_alert=False,
            reply_markup=Keyboards.ReturnKeyboard(),
        )
        return None


    @dp.callback_query_handler(text="get_private")
    async def GetPrivate(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        await bot.answer_callback_query(
            callback_query.id,
            text=Texts().private_text,
            reply_markup=Keyboards.BuyPrivateKeyboard(),
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
                callback_query.id, text=Texts().betausererror_text, show_alert=True
            )
            await bot.answer_callback_query(
                callback_query.id,
                text=Texts().betausererror_text,
                show_alert=False,
                reply_markup=Keyboards.ReturnKeyboard(),
            )
        return None


    @dp.callback_query_handler(text="donate")
    async def Donate(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        await callback_query.bot.edit_message_text(
            message_id=callback_query.message.message_id,
            chat_id=callback_query.message.chat.id,
            text=Texts().donate_text,
            reply_markup=Keyboards.DonateKeyboard(),
        )
        return None


    @dp.callback_query_handler(text="return")
    async def Return(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        await callback_query.bot.edit_message_text(
            message_id=callback_query.message.message_id,
            chat_id=callback_query.message.chat.id,
            text=Texts().menu_text,
            reply_markup=Keyboards.MenuKeyboard(),
        )
        return None


    @dp.callback_query_handler(text="rus")
    async def Russian(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        await callback_query.bot.edit_message_text(
            message_id=callback_query.message.message_id,
            chat_id=callback_query.message.chat.id,
            text=Texts().menu_text,
            reply_markup=Keyboards.MenuKeyboard(),
        )
        return None


    @dp.callback_query_handler(text="eng")
    async def English(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        await callback_query.bot.edit_message_text(
            message_id=callback_query.message.message_id,
            chat_id=callback_query.message.chat.id,
            text=Texts().menu_text,
            reply_markup=Keyboards.MenuKeyboard(),
        )
        return None


    # бесполезная хрень, но удалять страшно
    @dp.errors_handler(exception=MessageNotModified)
    async def message_not_modified_handler(update, error):
        return True




logger.success("bot started!")
executor.start_polling(Avoca.dp, skip_updates=True)
logger.warning("bot shutdown")