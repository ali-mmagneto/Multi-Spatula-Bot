# :d
from pyrogram import Client, filters
from KekikSpatula import Doviz
import json



@Client.on_message(filters.command("doviz"))
async def dovizzz(bot, message):
    dovizler = Doviz()
    sayi = 4
    say = 0
    text = "**Dövizler:**\n\n"
    for i in json.loads(dovizler.gorsel())["veri"]:
        say += 1
        text += f"**Birim**: `{i['birim']}`\n**Alış**: `{i['Gişe Alış']} TL`\n**Satış**: `{i['Gişe Satış']} TL`\n\n"
        if int(say) == int(sayi):
            await message.reply_text(text) 
