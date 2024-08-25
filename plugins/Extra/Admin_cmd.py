import asyncio
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton
from info import ADMINS

@Client.on_message(filters.command("admin_cmd") & filters.user(ADMINS))
async def admin_cmd(client, message):
    # Define the buttons
    buttons = [
        [KeyboardButton("/add_premium"), KeyboardButton("/premium_users")],
        [KeyboardButton("/add_redeem"), KeyboardButton("/broadcast")],
        [KeyboardButton("/grp_broadcast"), KeyboardButton("/remove_premium")],
        [KeyboardButton("/disable"), KeyboardButton("/leave")],
        [KeyboardButton("/ban"), KeyboardButton("/unban")],
        [KeyboardButton("/deleteall"), KeyboardButton("/delete")],
        [KeyboardButton("/Commands"), KeyboardButton("/restart")],
        [KeyboardButton("All These Commands Can Be Used Only By Admins.")],
        [KeyboardButton("⚡ powered by @JISSHU_BOTS")]
    ]
    reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
    
    # Send the reply message with the admin commands
    sent_message = await message.reply(
        "<b>Admin All Commands [auto delete 2 min] 👇</b>",
        reply_markup=reply_markup,
    )
    
    # Schedule the deletion of both the sent message and the command message after 2 minutes (120 seconds)
    await asyncio.sleep(120)
    await sent_message.delete()
    await message.delete()
