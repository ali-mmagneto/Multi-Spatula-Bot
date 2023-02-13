from pyrogram import Client, filters
import asyncio
from shazamio import Shazam

@Client.on_message(filters.command('shazam'))
async def shazamtara(bot, message):
    try:
        if message.reply_to_message.audio:
            ses = await bot.download_media(
                message = message.reply_to_message,
                file_name = f"{message.chat.id}.mp3")
            splitpath = ses.split("/downloads/")
            sestemp = splitpath[1]
            aranacak = f"downloads/{sestemp}"
            await bot.send_audio(
                chat_id = message.chat.id,
                audio = aranacak)
        elif message.reply_to_message.video:
            return
    except Exception as e:
        await message.reply_text(f"`{e}`")
