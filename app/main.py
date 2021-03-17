from flask import Flask, render_template, request
from telegram.ext import Updater
from telegram import error
import logging
from configparser import ConfigParser
import os


# set up parser for reading Telegram tokens from an INI file
parser = ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), r"config.ini"))

# read data from sysvars to program
recipient_chat_id = os.environ['RECIP_TOKEN']
bot_token = os.environ['SENDER_TOKEN']

# set up Telegram updater bot with token
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
updater = Updater(token= bot_token, use_context=True)

# main router
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def form():
    return render_template('form.html')

@app.route('/send', methods=['GET', 'POST'])
def send():

    requester_ip = request.remote_addr
    try:
        updater.bot.send_message(chat_id = recipient_chat_id, text="New message from " + requester_ip + ":\n" + request.form['to'])
    except error.BadRequest:
        return "Message too long!"
    return render_template('greeting.html', to=request.form['to'])

if __name__ == "__main__":
    app.run(debug=True)