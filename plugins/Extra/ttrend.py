from pyrogram import Client, filters
from info import ADMINS, DATABASE_URI
from database.trending import Jisshu_TOP
from pyrogram.types import ReplyKeyboardMarkup
import asyncio

# Initialize the @mr_jisshu
movie_series_db = Jisshu_TOP(DATABASE_URI)

@Client.on_message(filters.command("setlist") & filters.private & filters.user(ADMINS))
async def set_movie_series_names_command(client, message):
    # Extract the list of movie and series names from the command arguments
    try:
        command, *names = message.text.split(maxsplit=1)
    except ValueError:
        await message.reply("Pʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ʟɪsᴛ ᴏғ ᴍᴏᴠɪᴇ ᴀɴᴅ sᴇʀɪᴇs ɴᴀᴍᴇs ᴀғᴛᴇʀ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ.")
        return

    # Check if names are provided
    if not names:
        await message.reply("Pʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ʟɪsᴛ ᴏғ ᴍᴏᴠɪᴇ ᴀɴᴅ sᴇʀɪᴇs ɴᴀᴍᴇs ᴀғᴛᴇʀ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ.")
        return

    # Join the list of names into a single string separated by spaces
    names_string = " ".join(names)

    # Split the names string by commas and then capitalize each word in each name
    capitalized_names = ", ".join(" ".join(word.capitalize() for word in name.split()) for name in names_string.split(','))

    # Set the movie and series names in the database for the first suggestion
    await movie_series_db.set_movie_series_names(capitalized_names, 1)

    # Inform the user that the list has been set
    await message.reply("Tʜᴇ ʟɪsᴛ ᴏғ ᴍᴏᴠɪᴇ ᴀɴᴅ sᴇʀɪᴇs ɴᴀᴍᴇs ғᴏʀ ᴛʜᴇ sᴜɢɢᴇsᴛɪᴏɴ ʜᴀs ʙᴇᴇɴ ᴜᴘᴅᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ✅")

@Client.on_message(filters.command("trendlist"))
async def get_movie_series_names_command(client, message):
    # Get the current list of movie and series names from the database for suggestion 1
    current_names = await movie_series_db.get_movie_series_names(1)

    # Send the list to the user
    if current_names:
        response = "<b><u>Cᴜʀʀᴇɴᴛ ʟɪsᴛ ᴏғ ᴛᴏᴘ ᴛʀᴇɴᴅɪɴɢ:</u></b>\n"
        for i, name in enumerate(current_names, start=1):
            response += f"{i}. {name}\n"
        await message.reply(response.strip())
    else:
        await message.reply("Tʜᴇ ʟɪsᴛ ᴏғ ᴛᴏᴘ ᴛʀᴇɴᴅɪɴɢ ғᴏʀ ʙᴜᴛᴛᴏɴs ᴀʀᴇ ᴇᴍᴘᴛʏ ❌")

@Client.on_message(filters.command("clearlist") & filters.private & filters.user(ADMINS))
async def clear_movie_series_names_command(client, message):
    # Clear the movie and series names for suggestion 1
    await movie_series_db.clear_movie_series_names(1)
    await message.reply("Tʜᴇ ᴛᴏᴘ ᴛʀᴇɴᴅɪɴɢ ʟɪsᴛ ʜᴀs ʙᴇᴇɴ ᴄʟᴇᴀʀᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ✅")

# Command handler for "/trending"
@Client.on_message(filters.command("trend"))
async def trending_command(client, message):
    # Get movie and series names from the database for the trending list
    movie_series_names = await movie_series_db.get_movie_series_names(1)
    
    # Check if there are any names in the database
    if not movie_series_names:
        await message.reply("Tʜᴇʀᴇ ᴀʀᴇ ɴᴏ ᴍᴏᴠɪᴇ ᴏʀ sᴇʀɪᴇs ɴᴀᴍᴇs ᴀᴠᴀɪʟᴀʙʟᴇ ғᴏʀ ᴛʜᴇ ᴛᴏᴘ sᴇᴀʀᴄʜᴇs.")
        return

    # Create rows of buttons, with each row containing two buttons
    buttons = [movie_series_names[i:i + 2] for i in range(0, len(movie_series_names), 2)]

    # Create a ReplyKeyboardMarkup with buttons arranged in a grid layout
    spika = ReplyKeyboardMarkup(
        buttons,
        resize_keyboard=True
    )
    m=await message.reply_text("𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭, 𝐅𝐞𝐭𝐜𝐡𝐢𝐧𝐠 𝐓𝐨𝐩 𝐓𝐫𝐞𝐧𝐝𝐢𝐧𝐠.")
    await m.edit_text("𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭, 𝐅𝐞𝐭𝐜𝐡𝐢𝐧𝐠 𝐓𝐨𝐩 𝐓𝐫𝐞𝐧𝐝𝐢𝐧𝐠..")
    await m.edit_text("𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭, 𝐅𝐞𝐭𝐜𝐡𝐢𝐧𝐠 𝐓𝐨𝐩 𝐓𝐫𝐞𝐧𝐝𝐢𝐧𝐠...")
    await m.delete()        
    # Reply to the user with the keyboard
    await message.reply("<b>Hᴇʀᴇ ɪꜱ ᴛʜᴇ ᴛᴏᴘ ᴛʀᴇɴᴅɪɴɢ ʟɪꜱᴛ 👇</b>", reply_markup=spika)
