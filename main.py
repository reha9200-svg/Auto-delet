import telebot

TOKEN = "8722788286:AAE6sl19nX7ws105CEqflp3W18y8upeTHxs"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['new_chat_members', 'left_chat_member', 'group_chat_created'])
def delete_service_messages(message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
    except Exception as e:
        print(e)

bot.infinity_polling()
