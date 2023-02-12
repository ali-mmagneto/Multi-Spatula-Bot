# :d
from pyrogram import Client, filters
from KekikSpatula import HavaDurumu
from unidecode import unidecode
import json 

@Client.on_message(filters.command('hava'))
async def havaa(bot, message):
    try:
        ev = unidecode(message.text).split()
        if len(ev) < 3:
            await bot.send_message(message.chat.id, "Hatalı Kullanım :/ Doğru Kullanım Şu Şekilde:\n\n`/hava İstanbul Avcılar`") 
            return
        il = ev[1]
        ilce = ev[2]
        istek = HavaDurumu(il, ilce)
        text = ""
        for i in json.loads(istek.gorsel())["veri"]:
            fahrenayt1 = f"{i['derece']}"
            fahrenayt = int(fahrenayt1)
            text += f"{i['yer']} İçin:\nHava Durumu: `{i['derece']}` {fahrenayt} \nVakit: `{i['gun']}`"
        await bot.send_message(
           chat_id=message.chat.id,
           text=text)
    except Exception as e:
        await bot.send_message(
            chat_id=message.chat.id,
            text=f"`{e}`")
