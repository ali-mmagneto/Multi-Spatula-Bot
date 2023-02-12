# :d
from pyrogram import Client, filters
from KekikSpatula import Doviz
import json



@Client.on_message(filters.command("doviz"))
async def dovizzz(bot, message):
    dovizler = Doviz()
    text = "**Dövizler:**\n\n"
    for i in json.loads(dovizler.gorsel())["veri"]:
        text += f"**Birim**: `{i['birim']}`\n**Alış**: `{i['Gişe Alış']} TL`\nSatış: `{i['Gişe Satış']} TL`\n"
    await message.reply_text(text) 
