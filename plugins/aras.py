from pyrogram import Client, filters
from KekikSpatula import ArasKargo
import json


@Client.on_message(filters.command('araskargo'))
async def arasgetir(bot, message):
    try:
        mes = message.text.split(" ", 1)
        aranacak = mes[1]
        sorgu = ArasKargo(aranacak) 
        text = ""
        for i in json.loads(sorgu.gorsel())["veri"]:
            durum = f"{i['durum']['son_durum']}"
            teslimedildi = "TESLİM EDİLDİ"
            text += f"Kargo Cinsi: `{i['durum']['kargonun_cinsi']}`\nKargo Durumu: `{i['durum']['son_durum']}`\n"
            if durum == teslimedildi:
                text += f"Teslim Zamanı: {i['durum']['teslim_zaman']}\nTeslim Alan: {i['durum']['teslim_alan']}"
            else:
                text += f"\n**Hareketler**:\n**İşlem Zamanı**: `{i['hareketler']['islem_zaman']}`\n**İşlem Birimi**: `{i['hareketler']['islem_birim']}`\n**İşlem Açıklaması**: `{i['hareketler']['islem_aciklama']}`\n\n"
        await message.reply_text(text)
    except Exception as e:
        await message.reply_text(f"`{e}`")
