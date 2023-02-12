from pyrogram import Client, filters
from KekikSpatula import SonDepremler
import json
from unidecode import unidecode

@Client.on_message(filters.command('deprem'))
async def depremgetir(bot, message):
    try:
        link = unidecode(message.text).split()
        if len(link) == 1:
            sayi = 1
        else:
            sayi =  link[1]
        deprem = SonDepremler()
        text = "**Depremler**:\n\n"
        say = 0
        for i in json.loads(deprem.gorsel())["veri"]:
            enlem = f"{i['enlem']}"
            boylam = f"{i['boylam']}"
            adresurl = f"https://maps.google.com/maps?q={enlem},{boylam}"
            text += f"Yer: [{i['yer']}](adresurl)\nDerinlik: {i['derinlik']}\nBüyüklük: {i['ml']}\nTarih: {i['tarih']} {i['saat']}\n\n"
            say += 1
            if int(say) == int(sayi):
                await message.reply_text(text)
                return
    except Exception as e:
        await message.reply_text(f"`{e}`")
