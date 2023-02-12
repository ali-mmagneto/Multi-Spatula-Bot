# :d
from pyrogram import Client, filters 
from KekikSpatula import Ezan
import json
from unidecode import unidecode

@Client.on_message(filters.command('ezan'))
async def ezangetir(bot, message):
    try:
        ev = unidecode(message.text).split()
        if len(ev) < 2:
            await bot.send_message(message.chat.id, "Hatalı Kullanım :/ Doğru Kullanım Şu Şekilde:\n\n/ezan İstanbul") 
            return
        il = ev[1]
        istek = Ezan(il)
        text = ""
        for i in json.loads(istek.gorsel())["veri"]:
            text += f"{i['il']} İçin **Ezan Saatleri**:\n\n**İmsak**: `{i['imsak']}`\n**Güneş**: `{i['gunes']}`\n**Öğle**: `{i['ogle']}`\n**İkindi**: `{i['ikindi']}`\n**Akşam**: `{i['aksam']}`\n**Yatsı**: `{i['yatsi']}`"
        await bot.send_message(
           chat_id=message.chat.id,
           text=text)
    except Exception as e:
        await bot.send_message(
            chat_id=message.chat.id,
            text=f"`{e}`")
        
