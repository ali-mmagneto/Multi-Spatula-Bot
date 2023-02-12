# :d
from pyrogram import Client, filters
from KekikSpatula import Doviz
import json



@Bot.on_message(filters.command("doviz"))
async def dovizzz(bot, message):
    doviz_ = Doviz()
    text = "**Birim / Gişe Alış / Gişe Satış**\n\n"
    for key in json.loads(doviz_.gorsel())["veri"]:
        text += f"**{key['birim']}**: {key['Gişe Alış']} TL - {key['Gişe Satış']}\n"
    await message.reply_text(text) 
