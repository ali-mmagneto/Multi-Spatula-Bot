from pyrogram import Client, filters
import asyncio
from shazamio import Shazam
import json

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
            shazam = Shazam()
            out = await shazam.recognize_song(aranacak)
            bilgi = json.dumps(out)
            print(bilgi)
            i = bilgi["matches"]:
            text = f"Şarkı: {i['title']}\nSanatçı: {i['subtitle']}"
            await message.reply_text(f"{text}")
        elif message.reply_to_message.video:
            return
    except Exception as e:
        await message.reply_text(f"`{e}`")
