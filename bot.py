from telegram import Update, ChatMember
from telegram.ext import Updater, CommandHandler, CallbackContext
from config import TOKEN, CHANNEL_USERNAME
from database import init_db, add_user, is_premium, set_premium
from admin import broadcast, users

def is_user_joined_channel(bot, user_id):
    try:
        member = bot.get_chat_member(CHANNEL_USERNAME, user_id)
        return member.status in [ChatMember.MEMBER, ChatMember.OWNER, ChatMember.ADMINISTRATOR]
    except:
        return False

def start(update: Update, context: CallbackContext):
    user = update.effective_user
    add_user(user)

    if not is_user_joined_channel(context.bot, user.id):
        update.message.reply_text(f"📢 Please join our channel {CHANNEL_USERNAME} to use this bot.")
        return

    update.message.reply_text(
        f"Hi {user.first_name}, welcome to the TASHAN Prediction Bot!
Use /predict to get tips.
Use /subscribe to unlock premium."
    )

def predict(update: Update, context: CallbackContext):
    from fetcher import get_last_result, predict_next_color
    user_id = update.effective_user.id

    if not is_user_joined_channel(context.bot, user_id):
        update.message.reply_text(f"📢 Please join {CHANNEL_USERNAME} to use this feature.")
        return

    if not is_premium(user_id):
        update.message.reply_text("🔒 Premium only. Use /subscribe to unlock.")
        return

    last = get_last_result()
    prediction = predict_next_color(last)
    update.message.reply_text(f"🔮 Predicted Color: {prediction}")

def subscribe(update: Update, context: CallbackContext):
    set_premium(update.effective_user.id, True)
    update.message.reply_text("✅ You are now a premium user!")

def unsubscribe(update: Update, context: CallbackContext):
    set_premium(update.effective_user.id, False)
    update.message.reply_text("❌ You unsubscribed from premium.")

def main():
    init_db()
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("predict", predict))
    dp.add_handler(CommandHandler("subscribe", subscribe))
    dp.add_handler(CommandHandler("unsubscribe", unsubscribe))
    dp.add_handler(CommandHandler("broadcast", broadcast))
    dp.add_handler(CommandHandler("users", users))

    updater.start_polling()
    print("Bot running...")
    updater.idle()

if __name__ == '__main__':
    main()
