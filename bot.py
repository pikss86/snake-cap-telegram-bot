import os
from telegram.ext import Updater
from telegram.ext import CommandHandler


TOKEN = os.environ["SC_TELEGRAM_BOT_TOKEN"]
REQUEST_KWARGS = {
    'proxy_url': 'socks5://URL_OF_THE_PROXY_SERVER:PROXY_PORT',
    # Optional, if you need authentication:
    #'urllib3_proxy_kwargs': {
    #    'username': 'PROXY_USER',
    #    'password': 'PROXY_PASS',
    }
}
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()