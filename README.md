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

Once you've installed ngrok, you can run the following command to create a tunnel.

**On Windows**
```
ngrok.exe http 8443
```
**On Linux**
```
./ngrok http 8443
```

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

