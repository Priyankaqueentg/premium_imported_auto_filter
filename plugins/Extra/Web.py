import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from info import URL
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


# Command handler for /play command
@Client.on_message(filters.command('play'))
async def start(client, message):
    user_id = message.from_user.id
    username = message.from_user.username or 'JISSHU_BOTS'
    
    ads_id = 'ads'  
    
    if len(message.command) > 1:
        referrer_id = message.command[1]
    
    
    # Create referral link
    JsWeb_link = f'{URL}jisshu/?userId={user_id}&referrer={ads_id}&userName={username}'
    
    # Create InlineKeyboardMarkup with the referral link button
    reply_markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton('Play Free Premium', web_app=WebAppInfo(url=JsWeb_link))]]
    )
    await message.reply_sticker("CAACAgQAAxkBAAEBweZmi6IOPFaxaaGgMhIsi6DCrZhb5wAC6hMAAnaYYVD9OAxZrFc6EB4E")
    await message.reply_text(
        'College Coin & Get Free Premium...\n\n300 coin =  1 day Premium\n1400 coin =  5 day Premium\n1900 coin =  7 day Premium',
        reply_markup=reply_markup
    )

