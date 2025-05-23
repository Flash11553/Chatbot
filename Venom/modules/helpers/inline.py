from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL, PLAYLIST_NAME, SUPPORT_CHNL
from Venom import OWNER
from Venom import VenomX

DEV_OP = [
    [
        InlineKeyboardButton(text="Sahib 👨‍💻", user_id=OWNER),
        InlineKeyboardButton(text="Sohbet Qrupu 🇦🇿", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(
            text="🤍 Qrupa Əlavə Edin 🤍",
            url=f"https://t.me/{VenomX.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="Kanal 🤍", url=f"https://t.me/{PLAYLIST_NAME}"),
        InlineKeyboardButton(text="Playlist 🎧", url=f"https://t.me/{UPDATE_CHNL}"),
    ],
   
    [
       InlineKeyboardButton(text="Bot Əmrləri 🛠", callback_data="HELP"),
       InlineKeyboardButton(text="Haqqimda 🔍", callback_data="ABOUT"),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="🩶 Qrupa Əlavə Edin 🩶",
            url=f"https://t.me/{VenomX.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(
            text="✖️ Bağla",
            callback_data="CLOSE",
        ),
    ],
]


BACK = [
    [
        InlineKeyboardButton(text="🔙 Geri Qayıt", callback_data="BACK"),
    ],
]

HELP_BTN = [
    [
        InlineKeyboardButton(text="🐳 ᴄʜᴀᴛʙᴏᴛ 🐳", callback_data="CHATBOT_CMD"),
        InlineKeyboardButton(text="🎄 ᴀʟəᴛʟəʀ 🎄", callback_data="TOOLS_DATA"),
    ],
    [
        InlineKeyboardButton(text="✖️ Bağla", callback_data="CLOSE"),
        InlineKeyboardButton(text="🔙 Geri Qayıt", callback_data="BACK"),
    ],
]


CLOSE_BTN = [
    [
        InlineKeyboardButton(text="✖️ Bağla", callback_data="CLOSE"),
    ],
]


CHATBOT_ON = [
    [
        InlineKeyboardButton(text="ᴀᴋᴛiᴠ ᴇᴛ", callback_data=f"addchat"),
        InlineKeyboardButton(text="ᴅᴇᴀᴋᴛiᴠ ᴇᴛ", callback_data=f"rmchat"),
    ],
]


MUSIC_BACK_BTN = [
    [
        InlineKeyboardButton(text="sᴏᴏɴ", callback_data=f"soom"),
    ],
]

S_BACK = [
    [
        InlineKeyboardButton(text="🔙 Geri Qayıt", callback_data="SBACK"),
        InlineKeyboardButton(text="✖️ Bağla", callback_data="CLOSE"),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="🔙 Geri Qayıt", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="✖️ Bağla", callback_data="CLOSE"),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text="ᴋöᴍəᴋ 🔮", callback_data="HELP"),
        InlineKeyboardButton(text="✖️ Bağla", callback_data="CLOSE"),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(
            text="ᴋöᴍəᴋ 🔮", url=f"https://t.me/{VenomX.username}?start=help"
        ),
        InlineKeyboardButton(text="✖️ Bağla", callback_data="CLOSE"),
    ],
]


ABOUT_BTN = [
    [
        InlineKeyboardButton(text="✖️ Bağla", callback_data="CLOSE"),
        InlineKeyboardButton(text="🔙 Geri Qayıt", callback_data="BACK"),
    ],
]
