from pyrogram import Client, filters
import asyncio
from shazamio import Shazam
import json
import telegraph

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
            bilgiler = json.loads(bilgi)
            print(bilgiler)
            i = bilgiler["track"]
            photo = f"{i['images']['coverart']}"
            lyrics = f"{i['sections'][1]['text']}"
            print(lyrics)
            satir = "\n"
            soz = satir.join(lyrics)
            link = telegraph.create_page(
                    'Hey',
                    html_content=f"{lyrics}")
            text = f"**Şarkı**: [{i['title']}]({i['share']['href']})\n**Sanatçı**: {i['subtitle']}\n**Shazam İd**: {i['key']}\n"
            await bot.send_photo(
                chat_id = message.chat.id, 
                photo = photo, 
                caption = text)
        elif message.reply_to_message.video:
            return
    except Exception as e:
        await message.reply_text(f"`{e}`")
