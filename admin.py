from telegram import Update
from telegram.ext import CallbackContext
from config import ADMIN_IDS
from database import get_all_users, get_user_count

def is_admin(user_id):
    return user_id in 868578453

def broadcast(update: Update, context: CallbackContext):
    if not is_admin(update.effective_user.id):
        update.message.reply_text("❌ Unauthorized.")
        return

    message = ' '.join(context.args)
    if not message:
        update.message.reply_text("Use: /broadcast Your message")
        return

    sent = 0
    for uid in get_all_users():
        try:
            context.bot.send_message(uid, f"🎯 Admin Tip: {message}")
            sent += 1
        except:
            continue
    update.message.reply_text(f"✅ Sent to {sent} users.")

def users(update: Update, context: CallbackContext):
    if not is_admin(update.effective_user.id):
        update.message.reply_text("❌ Unauthorized.")
        return
    count = get_user_count()
    update.message.reply_text(f"👥 Total users: {count}")
