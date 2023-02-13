from PyMovieDb import IMDB
from pyrogram import Client, filters
from googletrans import Translator
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
        istek = imdbbilgi.get_by_name(aranacak, tv=True)
        data = json.loads(istek)
        caption = f"{istek}"
        text = ""
        oyuncular = ""
        for actors in data["actor"]:
            if data["actor"] == 0:
                oyuncular += "Bilinmiyor"
            else:
                oyuncular += f"`{actors['name']}`, "
        ceviri = Translator()
        konu_temp = f"{data['description']}"
        konu = ceviri.translate(konu_temp, dest='tr')
        imdburl = f"{data['url']}"
        photo = f"{data['poster']}"
        text += f"**İsim**: [{data['name']}]({imdburl})\n\n**Orijinal Dil**: `{data['review']['inLanguage']}`\n\n**Konu**: `{konu.text}`\n\n**Türler**:`{data['genre']}`\n\n**Oyuncular**: {oyuncular}\n\n**Yapım Tarihi**: `{data['review']['dateCreated']}`\n\n**İmdb Puanı**: `{data['rating']['ratingValue']}/10`" 
        await bot.send_photo(
            chat_id = message.chat.id, 
            photo = photo, 
            caption = text)
        await message.reply_text(caption)
    except Exception as e:
        await message.reply_text(f"`{e}`")
