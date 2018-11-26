import telegram
import sys
import os
from telegram.ext import Updater, CommandHandler
from pynput.keyboard import Key, Controller
from mss import mss

class Main():
    keyboard = Controller()

    def __init__(self, key, sendScreenshot):
        self.key = key
        self.sendScreenshot = sendScreenshot

    def printUsage(self):
        print("Usage: python3 main.py <key that's bound to fish> <(y/n) whether or not to send a screenshot after each fishing attempt>")
        os.exit()

    def getSecrets(self):
        f = open("../secrets.txt")
        for line in f.readlines():
            if line[0] == "#":
                continue
            else:
                return line

    def main(self):
        def screenshot(bot, update):
            with mss() as sct:
                print("Taking screenshot")
                filename = sct.shot()

                print("Sending screenshot")
                bot.send_photo(chat_id=update.message.chat_id, photo=open(filename, 'rb'))

                print("Deleteing screenshot")
                os.remove(filename)

        def fish(bot, update):
            print("Fishing")
            Main.keyboard.press(self.key)
            Main.keyboard.release(self.key)
            bot.send_message(chat_id=update.message.chat_id, text="no u")
            if (self.sendScreenshot):
                with mss() as sct:
                    print("Taking screenshot")
                    filename = sct.shot()

                    print("Sending screenshot")
                    bot.send_photo(chat_id=update.message.chat_id, photo=open(filename, 'rb'))

                    print("Deleteing screenshot")
                    os.remove(filename)

        secret = self.getSecrets()
        updater = Updater(token=secret)
        dispatcher = updater.dispatcher
        fish_handler = CommandHandler('fish', fish)
        screenshot_handler = CommandHandler('screenshot', screenshot)

        dispatcher.add_handler(fish_handler)
        dispatcher.add_handler(screenshot_handler)
        print("Polling")
        updater.start_polling()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()

    key = sys.argv[1]
    sendScreenshot = sys.argv[2].lower() == "y"
    print("Continuting with key:", key, "and with screenshot preference:", sendScreenshot)
    main = Main(key, sendScreenshot)
    main.main()