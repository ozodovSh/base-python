from telegram import Update
from telegram.ext import Updater, CommandHandler, ContextTypes
from parser import get_categories

TOKEN = "YOUR_BOT_TOKEN"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! /categories ni bosing")


async def categories(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cats = get_categories()

    if not cats:
        await update.message.reply_text("Kategoriya topilmadi")
        return

    text = "📦 Kategoriyalar:\n\n"
    for c in cats:
        text += f"• {c}\n"

    await update.message.reply_text(text)


app = Updater().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("categories", categories))

app.run_polling()