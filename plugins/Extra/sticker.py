from pyrogram import Client, filters

@Client.on_message(filters.command(["stickerid"]))
async def stickerid(client, message):
    # Check if the message is a reply and the replied message contains a sticker
    if message.reply_to_message and message.reply_to_message.sticker:
        sticker = message.reply_to_message.sticker
        await message.reply(
            f"**Sticker ID is**  \n `{sticker.file_id}` \n\n"
            f"**Unique ID is** \n\n`{sticker.file_unique_id}`", 
            quote=True
        )
    else:
        await message.reply("Oops! This is not a sticker file.", quote=True)
