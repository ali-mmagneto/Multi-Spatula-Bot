# :d
from pyrogram import Client, filters
from KekikSpatula import Doviz
import json

dovizler = Doviz()

@Client.on_message(filters.command("doviz"))
async def dovizgetir(bot, message):
    try:
        sayi = 4 # Benim (:d) Gerekli Bulduğum ilk 4 Doviz Bilgisini Getirir. 
        text = "Dövizler:\n"
        say = 0
        for i in json.loads(dovizler.gorsel())["veri"]:
            say += 1
            text += f"Birim: {i['birim']}\nAlış: {i['Gişe Alış']} TL\nSatış: {i['Gişe Satış']} Tl\n\n"
        if say == int(sayi):
            await bot.send_message(message.chat.id, text)
            return
    except Exception as e:
        await bot.send_message(message.chat.id, "`{e}`")
