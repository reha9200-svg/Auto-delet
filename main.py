 from pyrogram import Client, filters
from pyrogram.types import Message

# Direct credentials hardcoded taaki variable ka koi chakkar na rahe
api_id = 39116847
api_hash = "f06f5fa167d79eb30456b402f10cd12c"
bot_token = "8722788286:AAGoe51YgEuRWoCmJeuI75xHWTs_tLm7i8s"

app = Client(
    "tetrisalsi_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

@app.on_message(filters.group & (filters.new_chat_members | filters.left_chat_member))
async def delete_service_messages(client, message: Message):
    try:
        await message.delete()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    app.run()
