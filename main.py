import telebot

TOKEN = 8184887534:AAHS6AQBQa_P7XV4b8SfBGChLoPqJl9o80
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['new_chat_members', 'left_chat_member', 'group_chat_created'])
def delete_service_messages(message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
    except Exception as e:
        print(e)

bot.infinity_polling()
