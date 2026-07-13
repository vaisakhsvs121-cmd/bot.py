from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = "8774130816:AAFuqBNi5j2prTBrIkX7quvmh26dOZvCYRE"

CHANNELS = [
    "@channel2577999",
    "@smartdealsandoffers"
]

async def send_to_channels(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        text = update.message.text

        for channel in CHANNELS:
            await context.bot.send_message(
                chat_id=channel,
                text=text
            )

        await update.message.reply_text("✅ Message sent to both channels!")

app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_to_channels))

print("Bot is running...")
app.run_polling()
