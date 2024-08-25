import string
import random
from datetime import datetime, timedelta
import pytz
from pyrogram import Client, filters
from info import ADMINS, PREMIUM_LOGS
from utils import get_seconds  # Assuming get_seconds function is defined in utils module
from database.users_chats_db import db  # Assuming db functions are defined in users_chats_db module
from pyrogram.errors import MessageTooLong
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

VALID_REDEEM_CODES = {}  # Example in-memory storage for redeem codes

@Client.on_message(filters.command("add_redeem") & filters.user(ADMINS))
async def add_redeem_code(client, message):
    if len(message.command) == 2:
        time = message.command[1]
        code = generate_code()
        VALID_REDEEM_CODES[code] = time

        await message.reply_text(f"➩Redeem code added successfully!,\n➩Code: '<code>/redeem {code}</code>'\n➩Duration: {time}")
    else:
        await message.reply_text("<b>♻Usage:\n\n➩ <code>/add_redeem 1min</code>,\n➩ <code>/add_redeem 1hour</code>,\n➩ <code>/add_redeem 1day</code>,\n➩ <code>/add_redeem 1month</code>,\n➩ <code>/add_redeem 1year</code></b>")

@Client.on_message(filters.command("redeem"))
async def redeem_code(client, message):
    if len(message.command) == 2:
        redeem_code = message.command[1]

        if redeem_code in VALID_REDEEM_CODES:
            try:
                time = VALID_REDEEM_CODES.pop(redeem_code)  # Remove redeem code from dictionary after use
                user_id = message.from_user.id
                user = await client.get_users(user_id)
                seconds = await get_seconds(time)

                if seconds > 0:
                    expiry_time = datetime.now() + timedelta(seconds=seconds)
                    user_data = {"id": user_id, "expiry_time": expiry_time}
                    await db.update_user(user_data)

                    # Retrieve user and expiry time for confirmation message
                    data = await db.get_user(user_id)
                    expiry = data.get("expiry_time")
                    expiry_str_in_ist = expiry.astimezone(pytz.timezone("Asia/Kolkata")).strftime("%d-%m-%Y\n⏱️ ᴇxᴘɪʀʏ ᴛɪᴍᴇ : %I:%M:%S %p")

                    await message.reply_text(f"Premium activated successfully!\n\nUser: {user.mention}\nUser ID: {user_id}\nPremium Access: {time}\n\nExpiry Date: {expiry_str_in_ist}", disable_web_page_preview=True)

                    await client.send_message(
                        chat_id=user_id,
                        text=f"👋 ʜᴇʏ {user.mention},\nᴛʜᴀɴᴋ ʏᴏᴜ ꜰᴏʀ ᴘᴜʀᴄʜᴀꜱɪɴɢ ᴘʀᴇᴍɪᴜᴍ.\nᴇɴᴊᴏʏ !! ✨🎉\n\n⏰ ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴄᴇꜱꜱ : <code>{time}</code>\n⏳ ᴇxᴘɪʀʏ ᴅᴀᴛᴇ : {expiry_str_in_ist}", disable_web_page_preview=True
                    )

                    await client.send_message(PREMIUM_LOGS, text=f"#Redeem_Premium\n\n👤 ᴜꜱᴇʀ : {user.mention}\n⚡ ᴜꜱᴇʀ ɪᴅ : <code>{user_id}</code>\n⏰ ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴄᴇꜱꜱ : <code>{time}</code>\n⌛️ ᴇxᴘɪʀʏ ᴅᴀᴛᴇ : {expiry_str_in_ist}", disable_web_page_preview=True)

                else:
                    await message.reply_text("Invalid time format in redeem code.")

            except Exception as e:
                print(f"Error redeeming code: {str(e)}")
                await message.reply_text("An error occurred while redeeming the code. Please try again later.")

        else:
            await message.reply_text("Invalid Redeem Code or Expired.")

    else:
        await message.reply_text("Usage: /redeem code")

def generate_code(length=8):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))
