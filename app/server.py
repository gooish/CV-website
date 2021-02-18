from flask import Flask, render_template, request
from telegram.ext import Updater
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
updater = Updater(token='***REMOVED***', use_context=True)


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    return render_template('form.html')

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    updater.bot.send_message(chat_id = ***REMOVED***, text=request.form['to'])
    return render_template('greeting.html', to=request.form['to'])

if __name__ == "__main__":
    app.run(debug=True)