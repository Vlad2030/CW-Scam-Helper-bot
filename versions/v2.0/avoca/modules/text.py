privat_price = 500


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
