privat_price = 500

class ru_text:
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
    requestad_text = """
<b>Мы рады что ты присоединился в наше сообщество КВшеров!\n</b>
Предлагаем все тебе все наши каналы:
<a href="https://t.me/+aPzyHAQoMSE1NzYy">Avoca<a/> - наш чат
<a href="https://t.me/+s2wTdUM95eMzMDQy">CW SCAM<a/> - канал SCAM mode
<a href="https://t.me/CWMarketShop">CW MARKET<a/> - биржа аккаунтов Contract Wars

А также ты можешь пожертвовать немного:
<a href="https://www.donationalerts.com/r/avoca">Разработчику<a/>
<a href="https://www.qiwi.com/n/VLAD2030">На работу бота<a/>
"""
    private_text = f"Что-бы получить доступ к закрытому сообществу и знать информацию, а также ранние билды раньше всех, нужно купить доступ за <b>{privat_price}₽</b> по кнопке ниже и отписать @avoca_cw"

    ad_text = 'Сделайте пожертвование разработчикам'

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


class en_text:
    menu_text = "Welcome to the bot menu 👋"
    instruction_text = """
Full instructions where to download, install and use SCAM mode

<b>INSTALLATION:</b>
1. Download SCAM mode (attached below is a file with the current version of SCAM mode).
2. We unpack where it is convenient for you.
3. Find the folder with the game and throw the file Assembly-CSharp.dll at <code>CWClient\CWclient_Data\Managed</code> with a replacement (before that you need to close the game).

<b>USAGE:</b>
after you have successfully logged into the game, go to the console (the ~ key) and enter scam (activates SCAM mode).
all camouflage for any weapon and body kits are activated immediately, you don't even have to write scam.
Now let's go through the commands:
<code>scam</code> - enabling SCAM Mode
<code>scam_off</code> - disable SCAM Mode
<code>scam_hc</code> - transferring the arcade mode interface to hardcore + skills, heat, etc..
<code>proscam</code> - activates the commands scam_hc, devmode, freegun, full_thermal
<code>freegun</code> - free choice of weapons during combat
<code>devmode</code> - activates aim (hold down the N key) and vx
<code>addnickchanges 10</code> - adds 10 (you can enter any number) nickname shifts
<code>wtask ID</code> - purchase of wtasks (you need to specify the ID of the weapon and also cheat GP)
<code>GP 1000</code> - cheat GP (visual)
<code>SP 100</code> - cheat SP (visual)
<code>CR 100000</code> - cheat CR (visual)
<code>level 71</code> - makes you 71 lvl (visual)
<code>repa 500</code> - put 500 reputation (visual)
<code>exp 500</code> - put 500 experience (visual)
<code>wipewtask</code> - remove all wtask (visual)
<code>masterofarms</code> - put everything wtask (visual)
<code>knifedelay</code> - quick knife
<code>buyanov</code> - buyanov's eye - 100% accuracy (visual)
<code>hidden_server_access</code> - displaying hidden players and so on..
<code>addsnow</code> - adds snow to the map
<code>full_thermal</code> - thermal imager for the entire map (or the b key in proscam/devmode)
<code>show_enemy_nick</code> - display of nicknames when they are lit or hit by players
<code>connect_over_limit</code> - the ability to access maps when fully filled
<code>clear</code> - clears the console
<code>showcross</code> - crosshair
<code>s_debug</code> - list of servers
<code>targetframerate 144</code> - FPS limit to the number you need
<code>list</code> - shows the list of players on the server
<code>online</code> - shows the number of players in the game
<code>socialID</code> - your social network ID
<code>userID</code> - your ID in the game
<code>weapinfo</code> - information about weapons (only on the server)
<code>promo (XXXXX-XXXXX-XXXXX-XXXXX-XXXXX)</code> - promo code activation
<code>clearprofile</code> - reset profile (NOT visual)
<code>Fixed delta time -1</code> - fixed interval
<code>http_debug</code> - debugging http requests

All commands are written in the settings in the <b>SCAM info</b> tab
"""
    needsubscribe_text = "To receive you need to subscribe to certain channels"
    betausererror_text = "❌Beta tests are not being conducted at this time, come back later"
    error_text = "⛔Temporarily unavailable!"
    donate_text = "Choose the type of donation:"
    getscam_text = "You can get SCAM mode in this channel ↓"
    requestad_text = """
<b>We are glad that you have joined our community of QUakers!\n</b>
We offer everything to you all our channels:
<a href="https://t.me /+aPzyHAQoMSE1NzYy">Avoca<a/> - our chat
<a href="https://t.me /+s2wTdUM95eMzMDQy">CW SCAM<a/> - channel SCAM mode
<a href="https://t.me/CWMarketShop ">CW MARKET<a/> - Contract Wars account exchange

And you can also donate a little:
<a href="https://www.donationalerts.com/r/avoca ">To the developer<a/>
<a href="https://www.qiwi.com/n/VLAD2030 ">To work the bot<a/>
"""
    private_text = f"To get access to the closed community and know the information, as well as early builds before anyone else, you need to buy access for <b>{privat_price}₽</b> by clicking the button below and unsubscribe @avoca_cw"

    ad_text = 'Donate to developers'

    # button text
    instruction_buttontext = "📝Instruction"
    yourad_buttontext = "🎫Your ad could be here"
    getSCAM_buttontext = "📄Get SCAM"
    getonline_buttontext = "🌐Current Online"
    private_buttontext = "🔒Private channel"
    betauser_buttontext = "🆕Become a beta tester"
    cwmarket_buttontext = "📈Account Exchange"
    donate_buttontext = "💸Help the project"
    avoca_buttontext = "Donate to the creator"
    server_buttontext = "Donate for bot support"
    russian_buttontext = "🇷🇺"
    english_buttontext = "🇺🇸"
    CWSCAM_buttontext = "CW SCAM"
    buy_buttontext = 'Buy'
    back_buttontext = "↩Back"


class admin_text:
    # админ панель
    not_admin_text = 'ПОШЕЛ НАХУЙ ТЫ НЕ АДМИН!'
    admin_menu_text = 'Приветствую мой верховный правитель! Что желаете?'
    say_via_bot_text = 'Что напишем?'
    penalty_user_text = 'id_user time(h or d) reason'
    fuckoff_result_text = 'Пользователь послан!'
    moders_menu_text = 'Меню модеров'




    # админ кнопки
    say_buttontext = 'Писать от бота'
    ban_buttontext = 'Забанить'
    mute_buttontext = 'Замутить'
    fuckoff_buttontext = 'Послать нахуй'
    moder_buttontext = 'Модеры'
    addmoder_buttontext = 'Добавить модера'
    rmmoder_buttontext = 'Убрать модера'
    deletemoder_buttontext = 'Казнить модера'
    listmoder_buttontext = 'Список модеров'
    stat_buttontext = 'Статистика'