# :d
from pyrogram import Client, filters
from KekikSpatula import SonDakika
import json


@Client.on_message(filters.command("haber"))
async def habergetir(bot, message):
    haber = SonDakika()
    sayi = 1
    say = 0
    text = ""
    for i in json.loads(haber.gorsel())["veri"]:
        say += 1
        text += f"Başlık: {i['haber']}\n\nDetay: {i['link']}"
        photo = f"{i['gorsel']}"
        if say == sayi:
            await bot.send_photo(
                chat_id = message.chat.id, 
                photo = photo,
                caption = text)
            return
