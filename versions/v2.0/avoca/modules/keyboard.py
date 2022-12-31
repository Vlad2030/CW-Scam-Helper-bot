from . import text
from aiogram import types


def MenuKeyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton(
            text=text.instruction_buttontext,
            callback_data="get_instruction"
        ),
        types.InlineKeyboardButton(
            text=text.getSCAM_buttontext,
            callback_data="get_scam"
        ),
        types.InlineKeyboardButton(
            text=text.getonline_buttontext,
            callback_data="get_online"
        ),
        types.InlineKeyboardButton(
            text=text.private_buttontext,
            callback_data="get_private"
        ),
        types.InlineKeyboardButton(
            text=text.betauser_buttontext,
            callback_data="get_beta"
        ),
        types.InlineKeyboardButton(
            text=text.cwmarket_buttontext,
            url="https://t.me/CWMarketShop"
        ),
        types.InlineKeyboardButton(
            text=text.donate_buttontext,
            callback_data="donate"
        )
    )
    keyboard.add(
        types.InlineKeyboardButton(
            text=text.russian_buttontext,
            callback_data="rus"
        ),
        types.InlineKeyboardButton(
            text=text.english_buttontext,
            callback_data="eng"
        )
    )
    return keyboard


def ReturnKeyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton(
            text=text.back_buttontext,
            callback_data="return"
        )
    )
    return keyboard


def DonateKeyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton(
            text=text.avoca_buttontext,
            url="https://www.donationalerts.com/r/avoca"
        ),
        types.InlineKeyboardButton(
            text=text.server_buttontext,
            url="https://www.qiwi.com/n/VLAD2030"
        ),
        types.InlineKeyboardButton(
            text=text.back_buttontext,
            callback_data="return"
        )
    )
    return keyboard


def CWSCAMKeyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton(
            text=text.CWSCAM_buttontext,
            url="https://t.me/+s2wTdUM95eMzMDQy"
        ),
        types.InlineKeyboardButton(
            text=text.back_buttontext,
            callback_data="return"
            )
    )
    return keyboard


def BuyPrivateKeyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton(
            text=text.buy_buttontext,
            url="https://www.donationalerts.com/r/avoca"
        ),
        types.InlineKeyboardButton(
            text=text.back_buttontext,
            callback_data="return"
            )
    )
    return keyboard


def DonateADKeyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton(
            text=text.avoca_buttontext,
            url="https://www.donationalerts.com/r/avoca"
        ),
        types.InlineKeyboardButton(
            text=text.server_buttontext,
            url="https://www.qiwi.com/n/VLAD2030"
        )
    )
    return keyboard
