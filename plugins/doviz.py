# :d
from pyrogram import Client, filters
from KekikSpatula import Doviz
import json

dovizler = Doviz()

@Bot.on_message(filters.command("doviz"))
async def dovizgetir(bot, message):
    sayi = 4 # Benim (:d) Gerekli Bulduğum ilk 4 Doviz Bilgisini Getirir. 
    text = "Dövizler:\n"
    say = 0
    for i in json.loads(dovizler.gorsel())["veri"]:
        say += 1
        text += f"Birim: {i['birim']}\nAlış: {i['Gişe Alış']} TL\nSatış: {i['Gişe Satış']} Tl\n\n"
    if say == sayi:
        await message.reply_text(text)
        return
