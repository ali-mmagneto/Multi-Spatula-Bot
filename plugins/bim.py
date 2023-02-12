from pyrogram import Client, filters
from KekikSpatula import BimAktuel
import json

@Client.on_message(filters.command("bim"))
async def bimgetir(bot, message):
    try:
        aktuel = BimAktuel()
        text = ""
        for i in json.loads(aktuel.gorsel())["veri"]:
            text += f"{i['urun_baslik']\n\n**Fiyat**: {i['urun_fiyat']\n**Detay**: {i['urun_link']}"
            photo = f"{i['urun_gorsel']"
            await bot.send_photo(
                chat_id=message.chat.id, 
                photo=photo,
                caption=text)
    except Exception as e:
        await bot.send_message(message.chat.id, f"`{e}`")
