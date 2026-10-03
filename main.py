from pyrogram import Client, filters
from pyrogram.types import Message

# Apni details yahan dalein
api_id = 12345678      # Apni Telegram API ID dalein
api_hash = "YOUR_API_HASH"
bot_token = "8722788286:AAGoe51YgEuRwOcMJeul75xHWTs_tLm7i8s"

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.group & (filters.new_chat_members | filters.left_chat_member))
async def delete_service_messages(client, message: Message):
    try:
        await message.delete()
    except Exception as e:
        print(e)

app.run()
