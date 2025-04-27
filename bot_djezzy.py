import os
import telegram
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = os.getenv("7687040650:AAGzzmi4W6cqqijRa_iLrKSCwO-ZfuKizLs")  # التوكن يؤخذ من متغير بيئي

def start(update, context):
    keyboard = [
        [InlineKeyboardButton("سجّل عرض 3.5 جيجا", callback_data='register_offer')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('مرحبًا بك في بوت عروض جيزي!\nاختر ما تريد:', reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    query.answer()
    
    if query.data == 'register_offer':
        message = (
            "لتسجيل عرض 3.5 جيجا، اطلب الكود التالي من هاتفك:\n\n"
            "*720#\n\n"
            "أو استخدم تطبيق Djezzy للتسجيل."
        )
        query.edit_message_text(text=message)

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(button))

    print("البوت يعمل الآن...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()