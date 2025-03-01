from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL, PLAYLIST_NAME
from Venom import OWNER
from Venom import VenomX

DEV_OP = [
    [
        InlineKeyboardButton(text="Sahib 🤵‍♂️", user_id=OWNER),
        InlineKeyboardButton(text="Sohbet Qrupu 🇦🇿", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(
            text="➕ ǫʀᴜᴘᴀ əʟᴀᴠə ᴇᴛ ➕",
            url=f"https://t.me/{VenomX.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="Kanal 🤍", url=f"https://t.me/{PLAYLIST_NAME}"),
        InlineKeyboardButton(text="Playlist 🎧", url=f"https://t.me/{UPDATE_CHNL}"),
    ],   
    [
       InlineKeyboardButton(text="Kömək 🔮", callback_data="HELP"),
       InlineKeyboardButton(text="Support 🛠", url=f"https://t.me/{SUPPORT_GRP}"),), 
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="➕ ǫʀᴜᴘᴀ əʟᴀᴠə ᴇᴛ ➕",
            url=f"https://t.me/{VenomX.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(
            text="çɪxɪş 🚫",
            callback_data="CLOSE",
        ),
    ],
]


BACK = [
    [
        InlineKeyboardButton(text="🔙 ɢᴇʀi", callback_data="BACK"),
    ],
]


HELP_BTN = [
    [
        InlineKeyboardButton(text="🐳 ᴄʜᴀᴛʙᴏᴛ 🐳", callback_data="CHATBOT_CMD"),
        InlineKeyboardButton(text="🎄 ᴀʟəᴛʟəʀ 🎄", callback_data="TOOLS_DATA"),
    ],
    [
        InlineKeyboardButton(text="🔙 ɢᴇʀi", callback_data="BACK"),
        InlineKeyboardButton(text="çɪxɪş 🚫", callback_data="CLOSE"),
    ],
]


CLOSE_BTN = [
    [
        InlineKeyboardButton(text="çɪxɪş 🚫", callback_data="CLOSE"),
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
        InlineKeyboardButton(text="🔙 ɢᴇʀi", callback_data="SBACK"),
        InlineKeyboardButton(text="çɪxɪş 🚫", callback_data="CLOSE"),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="🔙 ɢᴇʀi", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="çɪxɪş 🚫", callback_data="CLOSE"),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text="ᴋöᴍəᴋ 🔮", callback_data="HELP"),
        InlineKeyboardButton(text="çɪxɪş 🚫", callback_data="CLOSE"),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(
            text="ᴋöᴍəᴋ 🔮", url=f"https://t.me/{VenomX.username}?start=help"
        ),
        InlineKeyboardButton(text="çɪxɪş 🚫", callback_data="CLOSE"),
    ],
]
