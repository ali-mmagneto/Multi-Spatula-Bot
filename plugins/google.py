from pyrogram import Client, filters
from KekikSpatula import Google
import json


@Client.on_message(filters.command('google'))
async def googleara(bot, message):
    try:
        mes = message.text.split(" ", 1)
        aranacak = mes[1]
        sayi = 5 # uygun gördüğüm gösterilecek arama sonucu sayısı
        google = Google(aranacak)
        say = 0
        text = "**Arama Sonuçların**:\n\n"
        for i in json.loads(google.gorsel())["veri"]:
            say += 1
            text += f"{say}-)\n**Başlık**: {i['baslik']}\n**Link**: {i['link']}\n**Açıklama**: {i['aciklama']}\n\n"
            if int(say) == int(sayi):
                await message.reply_text(text)
                return
    except Exception as e:
        await message.reply_text(f"`{e}`")
