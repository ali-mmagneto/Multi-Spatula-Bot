from pyrogram import Client, filters
from KekikSpatula import NobetciEczane
import json
from unidecode import unidecode

@Client.on_message(filters.command('nobetcieczane'))
async def eczanegetir(bot, message):
    try:
        link = unidecode(message.text).split()
        if len(link) < 3:
            await message.reply_text("Hatalı Kullanım :/ Doğru Kullanım\n\n/nobetcieczane İstanbul Kadıköy")
            return
        else:
            il =  link[1]
            ilce = link[2]
        text = ""
        nobetci = NobetciEczane(il, ilce)
        for i in json.loads(nobetci.gorsel())["veri"]:
            text += f"{i['ad']} {i['adres']}"
        await message.reply_text(text)
    except Exception as e:
        await message.reply_text(f"`{e}`")
