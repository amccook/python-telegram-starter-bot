#!/usr/bin/python2
from flask import Flask, request
import time
import json
import requests
import telegram


## ngrok https tunnel
HOST = '<your ngrok url>'   #ENTER YOUR NGROK URL HERE
PORT = 8443

## Telegram Bot Token
TOKEN = "<YOUR BOT TOKEN>"   #ENTER YOUR BOT TOKEN HERE

bot = telegram.Bot(TOKEN)
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    update = telegram.update.Update.de_json(request.get_json(force=True), bot)
    grab_message = update.message.text
    handle_message(grab_message, update)
    return 'OK'

def handle_message(message, update):
    if '/start' == message.lower():
        message_to_send = "Hi, I'm a telegram bot. Type /help to see what I can do."
        bot.sendMessage(chat_id=update.message.chat_id, text=message_to_send)
    elif '/help' == message.lower():
        message_to_send = "I can't do much! Add more elif statements to handle more commands."
        bot.sendMessage(chat_id=update.message.chat_id, text=message_to_send)
    else:
        message_to_send = "I don't understand your command. Try /help since that's the only command I respond to :)"
        bot.sendMessage(chat_id=update.message.chat_id, text=message_to_send)
        
def setWebhook():
    bot.setWebhook(webhook_url='https://%s/%s' % (HOST, TOKEN))

if __name__ == '__main__':
    setWebhook()
    time.sleep(5)
    app.run(host='0.0.0.0',
            port=PORT,
            debug=True)
