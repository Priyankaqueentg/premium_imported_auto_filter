# Don't Remove Credit @movie_file_20
# Subscribe YouTube Channel For Amazing Bot @movie_file_20
# Ask Doubt on telegram @KingVJ01

import time
import random
import psutil
from pyrogram import Client, filters

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_sticker("CAACAgIAAxkBAAEhzNdl6wzR3SsCw4dVU78FNpk0yCvn0gACKRgAAhP_2UkVxgiD_rlLGR4E") 
    await message.reply_text("𝖡𝗎𝖽𝖽𝗒 𝖨 𝖺𝗆 𝖠𝗅𝗂𝗏𝖾 :) 𝖧𝗂𝗍 /start\n\n𝖧𝗂𝗍 /stats To Check Bot Stats ;)\n\n𝖧𝗂𝗍 /ping 𝖳𝗈 𝖢𝗁𝖾𝖼𝗄 𝖡𝗈𝗍 𝖯𝗂𝗇𝗀 😉")
   


@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("⛈️")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    
    uptime_text = await get_system_uptime()
    
    await rm.edit(f"🏓 ᴘɪɴɢ: {time_taken_s:.3f} ms\n\n⏰ ᴜᴘᴛɪᴍᴇ: {uptime_text}")

async def get_system_uptime() -> str:
    boot_time_timestamp = psutil.boot_time()
    uptime_seconds = int(time.time()) - boot_time_timestamp
    uptime_days = uptime_seconds // (24 * 3600)
    uptime_hours = (uptime_seconds % (24 * 3600)) // 3600
    uptime_minutes = (uptime_seconds % 3600) // 60
    uptime_seconds = uptime_seconds % 60
    
    return f"{uptime_days} Day | {uptime_hours} Hour | {uptime_minutes} Min | {uptime_seconds} Sec"


