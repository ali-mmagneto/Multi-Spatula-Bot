from PyMovieDb import IMDB
from pyrogram import Client, filters
import requests
import json
from PIL import Image

@Client.on_message(filters.command('tmdb'))
async def tmdbgetir(bot, message):
    try:
        mes = message.text.split(" ", 1)
        if len(mes) == 1:
            await message.reply_text("Hatalı Kullanım :/ Doğru kullanım:\n\n`/tmdb Bullet Train`")
            return
        else:
            aranacak = mes[1]
        url = f"https://api.themoviedb.org/3/search/movie?api_key=f2d91ec751ea4b19fbdc66650232b17b&query={aranacak}&language=tr" 
        response = requests.get(url)
        data = response.json()
        text = ""
        for i in data["results"]:
            poster = f"{i['poster_path']}"
            photo1 = f"https://image.tmdb.org/t/p/w1280{poster}"
            img = Image.open(requests.get(photo1, stream = True).raw)
            img.save(f"{poster}")
            text += f"**İsim**: `{i['original_title']}`\n\nDil: `{i['original_language']}`\n\n**Konu**: `{i['overview']}`\n\n**Tmdb Puanı**: `{i['vote_average']}`/10\n\nOylayan Sayısı: `{i['vote_count']}`\n\n**Yayın Tarihi**: `{i['release_date']}`"
            await bot.send_photo(
                chat_id = message.chat.id,
                photo = poster,
                caption = text)
            text = ""
    except Exception as e:
        await message.reply_text(f"`{e}`") 
