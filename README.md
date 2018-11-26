# Telegram Fishing Bot

This is a simple bot that allows you to fish via Telegram. This is only working/available for Windows.


## Usage:

0. First install the requirements, ```pip install -r requirements.txt```
0. Then run the program ```python3 src/main.py <key that is bound to fishing> <(y/n -- defaults to no) whether or not to send screenshots after fishing attempts>


## Commands:

0. ```/fish``` - Send this to the bot to have them simulate pressing and releasing the defined key. If signified in startup (through the second argument), this will also send a screenshot after the fishing attempt.
0. ```/screenshot``` - Takes and sends a screenshot.