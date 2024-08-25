from pyrogram import Client, filters
import datetime
import time
from database.users_chats_db import db
from info import ADMINS
from utils import broadcast_messages, broadcast_messages_group
import asyncio
        
@Client.on_message(filters.command("broadcast") & filters.user(ADMINS) & filters.reply)
# https://t.me/JISSHU_BOTS
# https://t.me/Jisshu_support
