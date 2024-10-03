import telebot
from telebot import types

# Створи бота із використанням токену
bot = telebot.TeleBot('7612829192:AAEAG9bQprJbpGG7HI0kN1psxR__e3LM5UY')


# Функція, яка обробляє команду /start
@bot.message_handler(commands=['start'])
def start(message):
    telegram_id = message.from_user.id
    button = types.InlineKeyboardButton("Перейти до веб додатку", url=f"http://127.0.0.1:8000/employee/telegram/{telegram_id}/")
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button)
    bot.send_message(message.chat.id, "Статистика заробітньої плати", reply_markup=keyboard)

# Запуск бота
bot.polling()
