import os
import re
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

API_TOKEN = 'YOUR_API_TOKEN'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Send me a TXT file with video links.')

def handle_document(update: Update, context: CallbackContext) -> None:
    file = update.message.document.get_file()
    file.download('temp.txt')

    with open('temp.txt', 'r') as f:
        links = f.readlines()

    for link in links:
        link = link.strip()
        if re.match(r'https?://.*\.(mp4|avi|mov)', link):
            download_video(link)

    os.remove('temp.txt')
    update.message.reply_text('All videos have been downloaded.')

def download_video(link: str) -> None:
    try:
        response = requests.get(link, stream=True)
        filename = link.split("/")[-1]
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print(f'Downloaded: {filename}')
    except Exception as e:
        print(f'Failed to download {link}: {e}')

def main() -> None:
    updater = Updater(API_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.document.mime_type("text/plain"), handle_document))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
