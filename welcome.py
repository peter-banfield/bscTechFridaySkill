from flask import Flask
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def launched():
    return question('Welcome to the Alexa Skills Development Tech Friday!')

@ask.intent('Today')
def today():
    return statement('Today you will be learning how to write programs for me. '\
                    'Unlike programs you may have written before, users will not use a keyboard for interaction, but their voice.')

if __name__ == '__main__':
    app.run(debug=True)