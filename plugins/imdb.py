from PyMovieDb import IMDB
from pyrogram import Client, filters
import json

@Client.on_message(filters.command('imdb'))
async def imdbgetir(bot, message):
    try:
        sayi = 1
        mes = message.text.split(" ", 1)
        if len(mes) == 1:
            await message.reply_text("Hatalı Kullanım :/ Doğru kullanım:\n\n`/imdb Wandavision`")
        else:
            aranacak = mes[1]
        imdbbilgi = IMDB()
        istek = imdbbilgi.get_by_name(aranacak, tv=False)
        data = json.loads(istek)
        text = f"{data['name']}\n\{data['description']}" 
        await message.reply_text(text)
    except Exception as e:
        await message.reply_text(f"`{e}`")
