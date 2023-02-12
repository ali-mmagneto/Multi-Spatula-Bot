# :d
from pyrogram import Client, filters
from KekikSpatula import Doviz

dovizler = Doviz()

@Bot.on_message(filters.command("doviz"))
async def dovizgetir(bot, message):
    sayi = 4 # Benim (:d) Gerekli Bulduğum ilk 4 Doviz Bilgisini Getirir. 
    text = "Dövizler:\n"
    say = 0
    for key in json.loads(dovizler.gorsel())["veri"]:
        say += 1
        text += f"Birim: {key['birim']}\nAlış: {key['Gişe Alış']} TL\nSatış: {key['Gişe Satış']} Tl\n\n"
    if say == sayi:
        await message.reply_text(text)
        return
