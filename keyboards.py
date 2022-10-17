from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def generate_categories(categories):
    markup = ReplyKeyboardMarkup(row_width=4)
    buttons = []
    for category in categories:
        btn = KeyboardButton(text=category[0])
        buttons.append(btn)
    markup.add(*buttons)
    return markup


def generate_download(image_id):
    markup = InlineKeyboardMarkup()
    markup.add(
        # callback_data - 64 бит - 64 символа
        InlineKeyboardButton(text='Скачать в максимальном разрешении', callback_data=f'download_{image_id}')
    )
    return markup



