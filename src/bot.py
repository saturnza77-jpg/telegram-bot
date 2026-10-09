import telebot

from .llm import call_llm
from . import messages
from .db import DBHandler
from dotenv import load_dotenv
import os

load_dotenv()


bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))
db_handler = DBHandler()


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, messages.WELCOME_MESSAGE)


def is_valid_admin_reply(message):
    is_admin = message.user and message.user.id in os.getenv("ADMINS_USER_ID").split(
        ","
    )
    is_valid_chat = message.chat.username.lower() in os.getenv("VALID_CHATS").split(",")
    return is_admin and is_valid_chat


@bot.message_handler(func=lambda message: True)
def store_message(message):
    json_data = message.json
    db_handler.store_message(json_data)
    print("CHAT ID:", message.chat.id)
    print(f"Stored message with ID: {json_data.get('message_id')}")


@bot.message_reaction_handler()
def handle_reaction(message: telebot.types.MessageReactionUpdated):
    if not message.new_reaction:
        return

    reaction = message.new_reaction[-1].emoji
    if reaction not in ["👍"]:
        return

    message_data = db_handler.get_message(message.message_id)

    if message_data is None:
        return

    message_text = message_data.get("text")
    loading = bot.send_message(message.chat.id, "لطفا کمی صبر کنید...")
    # bot.reply_to(message, f"Preparing your answer...")
    response = call_llm(message_text)
    bot.edit_message_text("جواب حاضر است!", message.chat.id, loading.message_id)
    bot.send_message(message.chat.id, response)


@bot.message_handler(content_types=["text"])
def ai_reply(message):
    answer = call_llm(message.text)
    bot.reply_to(message, answer)


if __name__ == "__main__":
    print(messages.BOT_RUNNING)

    bot.infinity_polling(
        allowed_updates=["message", "message_reaction"],
    )
