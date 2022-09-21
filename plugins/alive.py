import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/ef5d2dcb34703be7a23eb.jpg",
        caption=f"""**
『It's a Music bot without lag and struck .
  It's a official Music bot of @AANDAVAR8064 
Nb : Bot and Userbot are locked by owner ,
     who wish to add this bot to your group,
     then , contact @AANDAVAR8064』
**""",
reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "『𝗖𝗛𝗔𝗡𝗡𝗘𝗟』", url=f"https://t.me/couplegiff"),
                    InlineKeyboardButton(
                        "『𝗜𝗡𝗦𝗧𝗔🎭𝗚𝗥𝗔𝗠』", url=f"https://www.instagram.com/insta_aandavar_official/"),
                    InlineKeyboardButton(
                        "『𝗙𝗔𝗖𝗘🌎𝗕𝗢𝗢𝗞』", url=f"https://www.facebook.com/smart.sathish.96592") 
                ]
            ]
        ),
     )
    
    
@Client.on_message(commandpro(["/start", "/alive", "blackcat"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/ef5d2dcb34703be7a23eb.jpg",
        caption=f"""**𝙾𝙵𝙵𝙸𝙲𝙸𝙰𝙻 𝐌𝐔𝐒𝐈𝐂 Bot of 𓄂AANDAVAR࿐ཽ༵✰**,
        it's A 💯% LAG AND STRUCK FREE MUSIC BOT , IT KEEP CLEAN YOUR CHAT WHEN IT WORK ON YOUR CHAT,3hrs Unlimited Playing without Lag,
        NB:- 24HRS ASSISTANCE OF bot
             (for anytime help:- [AANDAVAR8064](https://t.me/AANDAVAR8064)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "▲𝐅𝐀𝐌𝐈𝐋𝐘▼", url=f"https://t.me/couplegiff"),
                    InlineKeyboardButton(
                        "『𝐈𝐧𝐬𝐭𝐚🎭𝐆𝐫𝐚𝐦』", url=f"https://www.instagram.com/insta_aandavar_official/"),
                    InlineKeyboardButton(
                        "『𝐅𝐀𝐂𝐄🌎𝐁𝐎𝐎𝐊』", url=f"https://www.facebook.com/smart.sathish.96592")
                ]
            ]
        ),
    )

