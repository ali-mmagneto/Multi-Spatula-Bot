from pyrogram import Client, filters
import asyncio
from shazamio import Shazam
import json
import telegraph
from telegraph import Telegraph
from tiktok_downloader import tikdown

telegraph = Telegraph()
telegraph.create_account(short_name='deprembot')

@Client.on_message(filters.command('shazam'))
async def shazamtara(bot, message):
    try:
        if message.reply_to_message.audio or message.reply_to_message.video:
            mes = await message.reply_text("`Shazamda Arıyorum...`")
            ses = await bot.download_media(
                message = message.reply_to_message,
                file_name = f"{message.chat.id}.mp3")
            splitpath = ses.split("/downloads/")
            sestemp = splitpath[1]
            aranacak = f"downloads/{sestemp}"
            shazam = Shazam()
            out = await shazam.recognize_song(aranacak)
            await mes.edit("`Buldum Bilgileri Getiriyorum..`") 
            bilgi = json.dumps(out)
            bilgiler = json.loads(bilgi)
            print(bilgiler)
            i = bilgiler["track"]
            photo = f"{i['images']['coverart']}"
            lyrics = f"{i['sections'][1]['text']}"
            print(lyrics)
            satir = "\n"
            sarki = f"{i['title']}" 
            link = telegraph.create_page(
                    f"{sarki} Sözleri :d",
                    html_content=lyrics)
            text = f"**Şarkı**: [{i['title']}]({i['share']['href']})\n**Sanatçı**: {i['subtitle']}\n**Shazam İd**: {i['key']}\n**Lyrics**: {link['url']}"
            await bot.send_photo(
                chat_id = message.chat.id, 
                photo = photo, 
                caption = text)
            await mes.delete()
        elif message.reply_to_message.text:
            aranacak = message.reply_to_message.text
            d=tikdown(aranacak)
            print(d)
    except Exception as e:
        await message.reply_text(f"`{e}`")
