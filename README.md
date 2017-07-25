# python-telegram-starter-bot
A quick guide for setting up a telegram bot using ngrok.

## Getting Started

Please read through the prerequisites and installation instructions to get started. Overall, this bot should give you a template for writing more complex bots.

### Prerequisites
These are the known prerequisites I used to get this bot up and running.

1. Python 2.7.x
2. Telegram Bot
3. ngrok
4. Python packages:
    - virtualenv
    - Flask
    - python-telegram-bot
    - requests

## Installation
### 1. Check python Version

This bot was created using Python 2.7.x. I have not rewritten/tested on Python 3.x

Check your Python version
```
# python -V
Python 2.7.6
```

### 2. Create Telegram Bot

If you don't have one already, [join Telegram](https://telegram.org/) and create an account. Using the BotFather, [create a new bot](https://telegram.me/BotFather). 

Record your bot's TOKEN. It should look something like this: 123456789:AbCd3ef4GH6ijk8lmN5Opq5rSTUvwXYZZZZZ

### 3. Download and install ngrok

ngrok is useful if you don't have your own public HTTPS endpoint. Telegram needs an HTTP or HTTPS endpoint in order to setup a webhook for your bot. ngrok creates a tunnel so that Telegram can communicate with your localhost.

You can [download ngrok here](https://ngrok.com/download).

We'll review ngrok later in the Implementation section.

### 4. Install Python Packages

The python-telegram-starter-bot requires the following packages to be installed.

- virtualenv (More details on installation and usage [here](http://flask.pocoo.org/docs/0.12/installation/))
To install:
```
# sudo apt-get install python-virtualenv
```
Create a directory for your project and then create your virtualenv.
```
# mkdir /your/project/directory
# virtualenv venv
```
In your project's directory, enter your virtualenv
```
# . venv/bin/activate
```
**Be sure to remain in your virtualenv as you install Flask and the remaining packages**
- Flask (Same page from above on how to [install Flask](http://flask.pocoo.org/docs/0.12/installation/) or [reference Flask's documentation](http://flask.pocoo.org/docs/0.12/installation/))

In your working project directory AND with your virtualenv activated, install Flask
```
# pip install Flask
```
- python-telegram-bot (More details on this [package here](https://github.com/python-telegram-bot/python-telegram-bot))
```
# pip install python-telegram-bot
```
- requests (More details on this [package here](http://docs.python-requests.org/en/master/))
```
# pip install requests
```

## Implementation

1. With ngrok downloaded and installed, run:
**On Windows**
```
ngrok.exe http 8443
```
**On Linux**
```
./ngrok http 8443
```
Your tunnel will start and you will see a screen like this:
```
ngrok by @inconshreveable                              (Ctrl+C to quit)

Session Status       online
Version              2.2.8
Region               United States (us)
Web Interface        http://127.0.0.1:4040
Forwarding           http://8e4cbaf8.ngrok.io -> localhost:8443
Forwarding           https://8e4cbaf8.ngrok.io -> localhost:8443

Connections          ttl     opn     rt1     rt5     p50     p90
                     52      0       0.03    0.03    0.31    1.72
```

Record the ngrok url. In my example this is `8e4cbaf8.ngrok.io`

2. Using the code from [python-telegram-starter-bot.py](https://github.com/amccook/python-telegram-starter-bot/blob/master/python-telegram-starter-bot.py), provide the required details for HOST and TOKEN. 

Replace <YOUR NGROK URL> with your ngrok url. In my example, this would look like: `HOST = '8e4cbaf8.ngrok.io'`

Replace <YOUR BOT TOKEN> with your Telegram Bot Token. In my example, this would look like: `123456789:AbCd3ef4GH6ijk8lmN5Opq5rSTUvwXYZZZZZ`

3. Now run your bot.
```
# ./python-telegram-starter-bot.py
```
