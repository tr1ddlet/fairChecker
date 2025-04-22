import telebot
import random
import uuid

bot = telebot.TeleBot('7235514568:AAGqTofmFpRjZLsH-tPJbLJQ-_-VlH0UbFo')
SPECIAL_USER_ID = 858107352
SPECIAL_USER_ID2 = 7287199582
DANIAL_USER_ID = 872345007
DARIA_USER_ID = 1725536811
KANAT_USER_ID = 705261274

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Write /size to get your cock real size.")

@bot.message_handler(commands=['size'])
def send_random_number(message):
    user_id = message.from_user.id
    if user_id == SPECIAL_USER_ID:
        SPECIAL_NUMBER = random.randint(20, 80) 
        if( SPECIAL_NUMBER <= 50):
            bot.reply_to(message, f"WOW Real big cock energy! Your cock size is {SPECIAL_NUMBER}cm 💪🏼")
        elif( SPECIAL_NUMBER >50 and SPECIAL_NUMBER < 80):
            bot.reply_to(message, f"Godzilla would be scared. {SPECIAL_NUMBER} cm of destructive power 🐉")

    elif user_id == DANIAL_USER_ID or user_id == DARIA_USER_ID or user_id==SPECIAL_USER_ID2:
        LOSER_NUMBER = random.randint(1, 8) 
        if LOSER_NUMBER == 1:
            bot.reply_to(message, f"Scientists are still debating if this can legally be called a cock. Verdict: {LOSER_NUMBER}cm 🧪")
        elif LOSER_NUMBER > 1 and LOSER_NUMBER <= 4:
            bot.reply_to(message, f"Some say size doesn’t matter. In your case, we sure hope so. {LOSER_NUMBER}cm 🙏")
        elif LOSER_NUMBER > 4 and LOSER_NUMBER <= 6:
            bot.reply_to(message, f"Bro this ain't a cock, this is a typo 💀{LOSER_NUMBER}cm ?????")
        elif LOSER_NUMBER > 6 and LOSER_NUMBER <= 8:
            bot.reply_to(message, f"Cock? Bro that’s a USB stick: {LOSER_NUMBER}cm")

    elif user_id== KANAT_USER_ID:
        bot.reply_to(message, f"Your cock is 1cm. Not more, not less")
    else:
        number = random.randint(1, 20)
        bot.reply_to(message, f"Your cock size is  {number}cm")

from telebot.types import InlineQueryResultArticle, InputTextMessageContent
@bot.inline_handler(func=lambda query: True)
def inline_query(inline_query):
    user_id = inline_query.from_user.id

    if user_id == SPECIAL_USER_ID:
        SPECIAL_NUMBER = random.randint(20, 80) 
        if SPECIAL_NUMBER <= 50:
            text = f"WOW Real big cock energy! Your cock size is {SPECIAL_NUMBER}cm 💪🏼"
        else:
            text = f"Godzilla would be scared. {SPECIAL_NUMBER} cm of destructive power 🐉"

    elif user_id in [DANIAL_USER_ID, DARIA_USER_ID, SPECIAL_USER_ID2]:
        LOSER_NUMBER = random.randint(1, 8) 
        if LOSER_NUMBER == 1:
            text = f"Scientists are still debating if this can legally be called a cock. Verdict: {LOSER_NUMBER}cm 🧪"
        elif LOSER_NUMBER <= 4:
            text = f"Some say size doesn’t matter. In your case, we sure hope so. {LOSER_NUMBER}cm 🙏"
        elif LOSER_NUMBER <= 6:
            text = f"Bro this ain't a cock, this is a typo 💀{LOSER_NUMBER}cm ?????"
        else:
            text = f"Cock? Bro that’s a USB stick: {LOSER_NUMBER}cm"

    elif user_id == KANAT_USER_ID:
        text = f"Your cock is 1cm. Not more, not less"

    else:
        number = random.randint(1, 20)
        text = f"Your cock size is {number}cm"

    result = InlineQueryResultArticle(
    id=str(uuid.uuid4()),
    title=f'Measure your cock 📏 ({random.randint(1,100000)})',
    input_message_content=InputTextMessageContent(text)
)

    bot.answer_inline_query(inline_query.id, [result], cache_time=0)

bot.polling()