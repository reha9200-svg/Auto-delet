import os
from pyrogram import Client, filters
from pyrogram.types import Message

# Railway variables se values automatic uthayega
api_id = int(os.getenv("API_ID", "39116847"))
api_hash = os.getenv("API_HASH", "f06f5fa167d79eb30456b402f10cd12c")
bot_token = os.getenv("BOT_TOKEN", "8722788286:AAGoe51YgEuRWoCmJeuI75xHWTs_tLm7i8s")

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.group & (filters.new_chat_members | filters.left_chat_member))
async def delete_service_messages(client, message: Message):
    try:
        await message.delete()
    except Exception as e:
        print(e)

app.run()
