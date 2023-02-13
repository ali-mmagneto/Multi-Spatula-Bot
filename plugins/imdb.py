from PyMovieDb import IMDB
from pyrogram import Client, filters
import json

@Client.on_message(filters.command('imdb'))
async def imdbgetir(bot, message):
    try:
        mes = message.text.split(" ", 1)
        if len(mes) == 1:
            await message.reply_text("Hatalı Kullanım :/ Doğru kullanım:\n\n`/imdb Wandavision`")
        else:
            aranacak = mes[1]
        imdbbilgi = IMDB()
        istek = imdbbilgi.get_by_name(aranacak, tv=False)
        text = "" 
        for i in istek:
            text += f"{i['name'][0]}\n\n{i['description'][0]}"
        await message.reply_text(text)
    except Exception as e:
        await message.reply_text(f"`{e}`")
