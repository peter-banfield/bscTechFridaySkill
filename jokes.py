from flask import Flask
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, '/')

def get_dialog_state():
    return session['dialogState']

@ask.launch
def launched():
    return question('Welcome to Jokes! What kind of joke do you want to hear, a one liner or a knock knock joke?')\
        .reprompt('Sorry I missed that. Would you like to hear a one liner or a knock knock joke?')

@ask.intent('OneLiner')
def one_liner():
    return statement('Warning, keyboard not found. Press Enter to continue.')

@ask.intent('KnockKnock')
def knock_knock():
    dialog_state = get_dialog_state()
    if dialog_state != "COMPLETED":
        return delegate(speech=None)

    return statement('Welcome to 2017!')
