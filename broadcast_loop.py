import time
from telegram import Bot
from config import TOKEN
from database import get_all_users, is_premium
from fetcher import get_last_result, predict_next_color

def broadcast_prediction():
    bot = Bot(token=TOKEN)
    last_result = get_last_result()
    prediction = predict_next_color(last_result)

    for uid in get_all_users():
        if is_premium(uid):
            try:
                bot.send_message(uid, f"🔁 Auto Prediction: {prediction}")
            except:
                continue

def loop():
    while True:
        broadcast_prediction()
        time.sleep(60)

if __name__ == "__main__":
    loop()
