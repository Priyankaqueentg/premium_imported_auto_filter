from pyrogram import Client, filters
from pyrogram.types import BotCommand
from info import ADMINS

@Client.on_message(filters.command("commands") & filters.user(ADMINS))
async def set_commands(client, message):
    commands = [
        BotCommand("alive", "To Check Bot is Alive"),
        BotCommand("start", "To start the bot"),
        BotCommand("plan", "ᴄʜᴇᴄᴋ ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀꜱʜɪᴘ ᴘʟᴀɴꜱ"),
        BotCommand("most", "To Get Most Searches Button List"),
        BotCommand("trend", "To Get Top Trending Button List"),
        BotCommand("mostlist", "To Show Most Searches List"),
        BotCommand("trendlist", "𝖳𝗈 𝖦𝖾𝗍 𝖳𝗈𝗉 𝖳𝗋𝖾𝗇𝖽𝗂𝗇𝗀 𝖡𝗎𝗍𝗍𝗈𝗇 𝖫𝗂𝗌t"),
        BotCommand("myplan", "ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴜʀʀᴜɴᴛ ᴘʟᴀɴ"),
        BotCommand("redeem", "𝑇𝑜 𝑅𝑒𝑑𝑒𝑒𝑚 𝑃𝑟𝑒𝑚𝑖𝑢𝑚 𝐶𝑜𝑑𝑒"),
        BotCommand("refer", "To Refer Your Friend And Get Premium"),
        BotCommand("play", "Get Free Premium..."),
        BotCommand("stats", "ᴄʜᴇᴄᴋ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ"),
        BotCommand("id", "ɢᴇᴛ ᴛᴇʟᴇɢʀᴀᴍ ɪᴅ"),
        BotCommand("info", "ɢᴇᴛ ᴜꜱᴇʀ ɪɴꜰᴏ"),
        BotCommand("font", "To Generate Cool Fonts"),
        BotCommand("connect", "ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ"),
        BotCommand("settings", "ᴄʜᴀɴɢᴇ ʙᴏᴛ ꜱᴇᴛᴛɪɴɢꜱ"),
        BotCommand("admin_cmd", "Bot Admin All Commands")
    ]
    await client.set_bot_commands(commands)
    await message.reply("Set command successfully✅ ")
