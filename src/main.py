import telegram
from telegram.ext import Updater

def getSecrets():
    f = open("../secrets.txt")
    for line in f.readlines():
        if line[0] == "#":
            continue
        else:
            return line

def main():
    secret = getSecrets()
    updater = Updater(token=secret)

if __name__ == "__main__":
    main()