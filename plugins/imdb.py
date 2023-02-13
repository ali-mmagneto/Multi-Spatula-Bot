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
        datalar = json.loads(istek)
        text = ""
        for data in datalar:
            imdburl = f"{data['url']}"
            photo = f"{data['poster']}"
            oyuncular = f"`{data['actor']['name']}` "
            text += f"**İsim**: [{data['name']}]({imdburl})\n**Orijinal Dil**: `{data['review']['inLanguage']}`\n**Konu**: `{data['description']}`\n**Türler**:`{data['genre']}`\n**Oyuncular**: {oyuncular} **Yapım Tarihi**: `{data['review']['dateCreated']}`\n**İmdb Puanı**: `{data['rating']['ratingValue']}`" 
        await bot.send_photo(
            chat_id = message.chat.id, 
            photo = photo, 
            caption = text)
    except Exception as e:
        await message.reply_text(f"`{e}`")
