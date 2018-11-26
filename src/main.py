import telegram
from telegram.ext import Updater, CommandHandler


def getSecrets():
    f = open("../secrets.txt")
    for line in f.readlines():
        if line[0] == "#":
            continue
        else:
            return line

def fish(bot, update):
    print("Doing stuff")
    bot.send_message(chat_id=update.message.chat_id, text="no u")

def main():
    secret = getSecrets()
    updater = Updater(token=secret)
    dispatcher = updater.dispatcher
    fish_handler = CommandHandler('fish', fish)
    dispatcher.add_handler(fish_handler)
    print("Polling")
    updater.start_polling()


if __name__ == "__main__":
    main()