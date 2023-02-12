from pyrogram import Client

import os
import logging
from config import BOT_TOKEN, APP_ID, API_HASH, OWNER_ID
import time
from pyrogram.raw.all import layer
import pyrogram
from pyrogram import Client, __version__

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)
botStartTime = time.time()

plugins = dict(root='plugins')

Bot = Client(
    name='Saptula-Multi-Bot', 
    api_id=APP_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=plugins
    )

   
Bot.run()
