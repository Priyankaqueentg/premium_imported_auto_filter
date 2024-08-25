from datetime import datetime, timedelta
import pytz
from pyrogram import Client, filters
from pyrogram.types import Message
from database.users_chats_db import db  
from info import PREMIUM_LOGS
# @JISSHU_BOTS = @MR_JISSHU

def get_seconds(time_str):
    time_units = {
        'day': 86400,
        'hour': 3600,
        'min': 60,
        'month': 2592000,
        'year': 31536000
    }
    
    for unit in time_units:
        if time_str.endswith(unit):
            time_amount = int(time_str.replace(unit, ''))
            return time_amount * time_units[unit]
    return -1

@Client.on_message(filters.regex(r"#webpremium (\d+) (\d+\w+) (\d+)") & filters.chat(PREMIUM_LOGS))
async def add_premium_handler(client, message: Message):
    try:
        user_id = int(message.matches[0].group(1))
        time_str = message.matches[0].group(2)
        points = int(message.matches[0].group(3))  # Extract points from message
        
        seconds = get_seconds(time_str)
        if seconds <= 0:
            await message.reply_text("Invalid time format. Use formats like '1day', '1hour', '1min', '1month', '1year'.")
            return
        
        # Fetch current expiry time from the database
        data = await db.get_user(user_id)
        if data:
            expiry_time = data.get("expiry_time")
            if expiry_time:
                # Add the new duration to the existing expiry time
                expiry_time = expiry_time + timedelta(seconds=seconds)
            else:
                # If no expiry time, set it to the current time plus the new duration
                expiry_time = datetime.now() + timedelta(seconds=seconds)
        else:
            # If user is not in the database, set the expiry time to the current time plus the new duration
            expiry_time = datetime.now() + timedelta(seconds=seconds)
        
        user_data = {"id": user_id, "expiry_time": expiry_time, "points": points}  # Include points in user data
        await db.update_user(user_data)

        user = await client.get_users(user_id)
        current_time = datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%d-%m-%Y\n⏱️ ᴊᴏɪɴɪɴɢ ᴛɪᴍᴇ : %I:%M:%S %p")
        expiry_str = expiry_time.astimezone(pytz.timezone("Asia/Kolkata")).strftime("%d-%m-%Y\n⏱️ ᴇxᴘɪʀʏ ᴛɪᴍᴇ : %I:%M:%S %p")
        
        reply_text = (
            f"ᴘʀᴇᴍɪᴜᴍ ᴀᴅᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜰᴜʟʟʏ ✅\n\n"
            f"👤 ᴜꜱᴇʀ : {user.mention}\n"
            f"⚡ ᴜꜱᴇʀ ɪᴅ : <code>{user_id}</code>\n"
            f"💰 ʀᴇᴅᴇᴇᴍɪɴɢ ᴘᴏɪɴᴛꜱ : <code>{points}</code>\n"
            f"⏰ ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴄᴇꜱꜱ : <code>{time_str}</code>\n\n"
            f"⏳ ᴊᴏɪɴɪɴɢ ᴅᴀᴛᴇ : {current_time}\n\n"
            f"⌛️ ᴇxᴘɪʀʏ ᴅᴀᴛᴇ : {expiry_str}"
        )
        
        await message.reply_text(reply_text, disable_web_page_preview=True)
        await client.send_message(user_id, text=f"👋 ʜᴇʏ {user.mention},\nᴛʜᴀɴᴋ ʏᴏᴜ ꜰᴏʀ ᴘᴜʀᴄʜᴀꜱɪɴɢ ᴘʀᴇᴍɪᴜᴍ.\nᴇɴᴊᴏʏ !! ✨🎉\n\n💰 ʀᴇᴅᴇᴇᴍɪɴɢ ᴘᴏɪɴᴛꜱ : <code>{points}</code>\n⏰ ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴄᴇꜱꜱ : <code>{time_str}</code>\n⏳ ᴊᴏɪɴɪɴɢ ᴅᴀᴛᴇ : {current_time}\n\n⌛️ ᴇxᴘɪʀʏ ᴅᴀᴛᴇ : {expiry_str}", disable_web_page_preview=True)
        
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")
