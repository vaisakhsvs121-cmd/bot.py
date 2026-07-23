from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = "8774130816:AAFuqBNi5j2prTBrIkX7quvmh26dOZvCYRE"

CHANNELS = [
    "@channel2577999",
    "@smartdealsandoffers"
]
async def send_to_channels(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:

        lines = update.message.text.strip().split("\n")

product = lines[0] if len(lines) > 0 else ""
price = lines[1] if len(lines) > 1 else ""
link = "\n".join(lines[2:]) if len(lines) > 2 else ""

        formatted = f"""🔥🔥 HOT DEAL ALERT 🔥🔥

🛍️ Product : {product}

💸 Offer Price : {price}

🔗 Buy Now:
{link}

⚡ Hurry! Limited-Time Deal

━━━━━━━━━━━━━━━━━━
📢 Join @smartdealsandoffers
❤️ Share with Friends
━━━━━━━━━━━━━━━━━━
"""

        for channel in CHANNELS:
            await context.bot.send_message(
                chat_id=channel,
                text=formatted
            )

        await update.message.reply_text("✅ Deal posted successfully!")

app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_to_channels))

print("Bot is running...")
app.run_polling()
