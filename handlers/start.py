import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.delete()
    await message.reply_sticker("CAACAgUAAxkBAAEENxZiNtPdibVkMsjLZrUG9NK4hotHQgAC2wEAAoM12VSdN9ujxVtnUyME")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━━━━━━━━━━━━━━━━━━
💔 هلا عمري {message.from_user.mention()} !
        انا بوت اسمي ايزوكي استطيع تشغيل الاغاني في المكالمه المرئيه
يمكنني التشغيل بصوت رائع وبدون اي مشاكل او تقطيع في الاغنيه
 اضفني الى مجموعتك وامنحني الصلاحيات لكي اعمل بشكل صحيح
______________________________________
┣★    اضفني 1.                       |
┣★  ارسل انضم لأنضمام المساعد 2
┣★ قم بلضغط على زر الاوامر لمعرفه عمل البوت 3
_____________________________________|
=====================================
     [المطور](t.me\{OWNER_USERNAME})
━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اضفني الى مجموعتك", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "مطور البوت", url=f"https://t.me/{OWNER_USERNAME}"
                    ),
                    InlineKeyboardButton(
                        "قناة الدعم", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],[
                    InlineKeyboardButton(
                        "الاوامر", url=f"https://telegra.ph/%D8%A7%D9%87%D9%84%D8%A7-%D8%B9%D9%85%D8%B1%D9%8A-%D9%87%D8%A7%D9%8A-%D8%A7%D9%88%D8%A7%D9%85%D8%B1-%D8%A7%D9%84%D8%A8%D9%88%D8%AA-07-03"
                    ),
                    InlineKeyboardButton(
                        "قناة البوت الرسمية", url="https://t.me/{SUPPORT_GROUP}"
                    )]
            ]
       ),
    )

