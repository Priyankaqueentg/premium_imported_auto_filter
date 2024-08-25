import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, Message
from info import LOG_CHANNEL

@Client.on_message(filters.private & filters.photo)
async def screenshot_handler(client, message):
    # Add buttons for forwarding or canceling
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Yes ✅", callback_data="yes"),
         InlineKeyboardButton("No 🚫", callback_data="no")]
    ])

    # Send confirmation message with buttons
    await message.reply_text(
        "Are you sure, You want to send this screenshot to the Admins?",
        reply_markup=keyboard,
        quote=True  # Add this line to make sure the buttons are in the same context as the photo
    )

@Client.on_callback_query(filters.regex("yes"))
async def yes_callback(client, callback_query):
    try:
        # Get user details
        user = callback_query.from_user
        user_details = (
            f"User ID: {user.id}\n"
            f"Username: @{user.username}\n"
            f"Name: {user.first_name} {user.last_name if user.last_name else ''}"
        )

        # Forward the screenshot to the log channel with user details
        await client.send_photo(
            chat_id=LOG_CHANNEL,
            photo=callback_query.message.reply_to_message.photo.file_id,
            caption=user_details
        )

        # Notify the user
        await callback_query.message.edit_text("Screenshot sent to the Admins.")
    except Exception as e:
        await callback_query.message.edit_text(f"An error occurred: {e}")

@Client.on_callback_query(filters.regex("no"))
async def no_callback(client, callback_query):
    try:
        # Delete the confirmation message
        await callback_query.message.delete()
    except Exception as e:
        await callback_query.message.reply_text(f"An error occurred: {e}")

    # Send cancellation message
    await callback_query.message.reply_text("Your process has been cancelled. 🫠")
