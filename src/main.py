import telegram
import sys
import os
from telegram.ext import Updater, CommandHandler
from pynput.keyboard import Key, Controller

class Main():
    keyboard = Controller()

    def __init__(self, key):
        self.key = key

    def printUsage(self):
        print("Usage: python3 main.py <key that's bound to fish>")
        os.exit()

    def getSecrets(self):
        f = open("../secrets.txt")
        for line in f.readlines():
            if line[0] == "#":
                continue
            else:
                return line

    def main(self):
        def fish(bot, update):
            print("Doing stuff")
            Main.keyboard.press(self.key)
            Main.keyboard.release(self.key)
            ot.send_message(chat_id=update.message.chat_id, text="no u")

        secret = self.getSecrets()
        updater = Updater(token=secret)
        dispatcher = updater.dispatcher
        fish_handler = CommandHandler('fish', fish)
        dispatcher.add_handler(fish_handler)
        print("Polling")
        updater.start_polling()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()

    key = sys.argv[1]
    print("Continuting with key:", key)
    main = Main(key)
    main.main()