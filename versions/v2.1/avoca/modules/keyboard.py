from . import text
from aiogram import types

class ru_keyboard:
    def ruMenuKeyboard():
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            types.InlineKeyboardButton(
                text=text.ru_text.instruction_buttontext,
                callback_data="ru_get_instruction"
            ),
            types.InlineKeyboardButton(
                text=text.ru_text.getSCAM_buttontext,
                callback_data="ru_get_scam"
            ),
            types.InlineKeyboardButton(
                text=text.ru_text.getonline_buttontext,
                callback_data="ru_get_online"
            ),
            types.InlineKeyboardButton(
                text=text.ru_text.private_buttontext,
                callback_data="ru_get_private"
            ),
            types.InlineKeyboardButton(
                text=text.ru_text.betauser_buttontext,
                callback_data="ru_get_beta"
            ),
            types.InlineKeyboardButton(
                text=text.ru_text.cwmarket_buttontext,
                url="https://t.me/CWMarketShop"
            ),
            types.InlineKeyboardButton(
                text=text.ru_text.donate_buttontext,
                callback_data="ru_donate"
            )
        )
        keyboard.add(
            types.InlineKeyboardButton(
                text=text.ru_text.russian_buttontext,
                callback_data="rus"
            ),
            types.InlineKeyboardButton(
                text=text.ru_text.english_buttontext,
                callback_data="eng"
            )
        )
        return keyboard


    def ruReturnKeyboard():
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(
            types.InlineKeyboardButton(
                text=text.ru_text.back_buttontext,
                callback_data="ru_return"
            )
        )
        return keyboard


    def ruDonateKeyboard():
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            types.InlineKeyboardButton(
                text=text.ru_text.avoca_buttontext,
                url="https://www.donationalerts.com/r/avoca"
            ),
            types.InlineKeyboardButton(
                text=text.ru_text.server_buttontext,
                url="https://www.qiwi.com/n/VLAD2030"
            ),
            types.InlineKeyboardButton(
                text=text.ru_text.back_buttontext,
                callback_data="ru_return"
            )
        )
        return keyboard


    def ruCWSCAMKeyboard():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            types.InlineKeyboardButton(
                text=text.ru_text.CWSCAM_buttontext,
                url="https://t.me/+s2wTdUM95eMzMDQy"
            ),
            types.InlineKeyboardButton(
                text=text.ru_text.back_buttontext,
                callback_data="ru_return"
                )
        )
        return keyboard


    def ruBuyPrivateKeyboard():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            types.InlineKeyboardButton(
                text=text.ru_text.buy_buttontext,
                url="https://www.donationalerts.com/r/avoca"
            ),
            types.InlineKeyboardButton(
                text=text.ru_text.back_buttontext,
                callback_data="ru_return"
                )
        )
        return keyboard


    def ruDonateADKeyboard():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            types.InlineKeyboardButton(
                text=text.ru_text.avoca_buttontext,
                url="https://www.donationalerts.com/r/avoca"
            ),
            types.InlineKeyboardButton(
                text=text.ru_text.server_buttontext,
                url="https://www.qiwi.com/n/VLAD2030"
            )
        )
        return keyboard


class en_keyboard:
    def enMenuKeyboard():
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            types.InlineKeyboardButton(
                text=text.en_text.instruction_buttontext,
                callback_data="en_get_instruction"
            ),
            types.InlineKeyboardButton(
                text=text.en_text.getSCAM_buttontext,
                callback_data="en_get_scam"
            ),
            types.InlineKeyboardButton(
                text=text.en_text.getonline_buttontext,
                callback_data="en_get_online"
            ),
            types.InlineKeyboardButton(
                text=text.en_text.private_buttontext,
                callback_data="en_get_private"
            ),
            types.InlineKeyboardButton(
                text=text.en_text.betauser_buttontext,
                callback_data="en_get_beta"
            ),
            types.InlineKeyboardButton(
                text=text.en_text.cwmarket_buttontext,
                url="https://t.me/CWMarketShop"
            ),
            types.InlineKeyboardButton(
                text=text.en_text.donate_buttontext,
                callback_data="en_donate"
            )
        )
        keyboard.add(
            types.InlineKeyboardButton(
                text=text.en_text.russian_buttontext,
                callback_data="rus"
            ),
            types.InlineKeyboardButton(
                text=text.en_text.english_buttontext,
                callback_data="eng"
            )
        )
        return keyboard


    def enReturnKeyboard():
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(
            types.InlineKeyboardButton(
                text=text.en_text.back_buttontext,
                callback_data="en_return"
            )
        )
        return keyboard


    def enDonateKeyboard():
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            types.InlineKeyboardButton(
                text=text.en_text.avoca_buttontext,
                url="https://www.donationalerts.com/r/avoca"
            ),
            types.InlineKeyboardButton(
                text=text.en_text.server_buttontext,
                url="https://www.qiwi.com/n/VLAD2030"
            ),
            types.InlineKeyboardButton(
                text=text.en_text.back_buttontext,
                callback_data="en_return"
            )
        )
        return keyboard


    def enCWSCAMKeyboard():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            types.InlineKeyboardButton(
                text=text.en_text.CWSCAM_buttontext,
                url="https://t.me/+s2wTdUM95eMzMDQy"
            ),
            types.InlineKeyboardButton(
                text=text.en_text.back_buttontext,
                callback_data="en_return"
                )
        )
        return keyboard


    def enBuyPrivateKeyboard():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            types.InlineKeyboardButton(
                text=text.en_text.buy_buttontext,
                url="https://www.donationalerts.com/r/avoca"
            ),
            types.InlineKeyboardButton(
                text=text.en_text.back_buttontext,
                callback_data="en_return"
                )
        )
        return keyboard


    def enDonateADKeyboard():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            types.InlineKeyboardButton(
                text=text.en_text.avoca_buttontext,
                url="https://www.donationalerts.com/r/avoca"
            ),
            types.InlineKeyboardButton(
                text=text.en_text.server_buttontext,
                url="https://www.qiwi.com/n/VLAD2030"
            )
        )
        return keyboard


class admin_keyboard:
    def adminMenuKeyboard():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            types.InlineKeyboardButton(
                text=text.admin_text.say_buttontext,
                callback_data="say_via_bot"
            ),
            types.InlineKeyboardButton(
                text=text.admin_text.ban_buttontext,
                callback_data="ban_user"
            ),
            types.InlineKeyboardButton(
                text=text.admin_text.mute_buttontext,
                callback_data="mute_user"
            ),
            types.InlineKeyboardButton(
                text=text.admin_text.fuckoff_buttontext,
                callback_data="fuckoff_user"
            ),
            types.InlineKeyboardButton(
                text=text.admin_text.moder_buttontext,
                callback_data="moders"
            ),
            types.InlineKeyboardButton(
                text=text.admin_text.stat_buttontext,
                callback_data="statistics"
            ),
        )
        return keyboard


    def adminMenuReturnKeyboard():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            types.InlineKeyboardButton(
                text=text.ru_text.back_buttontext,
                callback_data="admin_menu"
            )
        )
        return keyboard


    def adminModersMenuKeyboard():
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            types.InlineKeyboardButton(
                text=text.admin_text.addmoder_buttontext,
                callback_data="admin_addmoder"
            ),
            types.InlineKeyboardButton(
                text=text.admin_text.rmmoder_buttontext,
                callback_data="admin_rmmoder"
            ),
            types.InlineKeyboardButton(
                text=text.admin_text.deletemoder_buttontext,
                callback_data="admin_deletemoder"
            ),
            types.InlineKeyboardButton(
                text=text.admin_text.listmoder_buttontext,
                callback_data="admin_listmoder"
            ),
            types.InlineKeyboardButton(
                text=text.ru_text.back_buttontext,
                callback_data="admin_menu"
            )
        )
        return keyboard