import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8282166516:AAH43Tx0D2A2dyQMzZBN2a_ABf0oSdzS6xc"
ADMIN_ID = 1179417059  

bot = telebot.TeleBot(TOKEN)

# --- Команда /start ---
@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton("Сделать заказ")
    markup.add(btn)
    bot.send_message(message.chat.id, "Привет! Хочешь сделать заказ?", reply_markup=markup)

# --- Обработка нажатия кнопки ---
@bot.message_handler(func=lambda message: message.text == "Сделать заказ")
def ask_quantity(message):
    bot.send_message(message.chat.id, "Сколько штук нужно? Напиши число.")
    bot.register_next_step_handler(message, get_quantity)

# --- Обработка количества ---
def get_quantity(message):
    if not message.text.isdigit():
        bot.send_message(message.chat.id, "❗ Введите число (только цифры)")
        return bot.register_next_step_handler(message, get_quantity)

    quantity = message.text

    # Сообщение админу (ТЕБЕ)
    bot.send_message(ADMIN_ID, f"📦 Новый заказ!\nОт пользователя: @{message.from_user.username}\nКоличество: {quantity}")

    # Сообщение пользователю
    bot.send_message(message.chat.id, "Спасибо! Заказ отправлен ✅")

bot.infinity_polling()
