from flask import Flask #import flask
from flask_ask import Ask, statement, question, convert_errors, request, context, session, version
import logging

app = Flask(__name__)
ask = Ask(app, '/')
log = logging.getLogger()

@ask.launch #launch decorator handles launch requests
def launched():
    return question('Welcome to Foo')

@ask.intent('HelloWorldIntent') #intent decorator handles intent requests
def hello():
    return statement('Hello, world')

@ask.session_ended #session_ended decorator handles session endded request
def sesssion_ended():
    return "{}", 200

#Launch and intent requests can both start sessions. 
@ask.on_session_started #Avoid duplicate code with the on_session_started callback
def new_session():
    log.info('new session started')

@ask.intent('WeatherIntent', mapping={'city': 'City'}) #mapping fixes when slots and parameter names are different
def weather(city):
    return statement('I predict great weather for {}'.format(city))

@ask.intent('HelloIntent', default={'name': 'World'}) #sets default value for a slot
def hello(name):
    return statement('Hello, {}'.format(name))

@ask.intent('AddIntent', convert={'x': int, 'y': int}) #use convert to change from strings to python data types
def add(x, y):
    z = x + y
    return statement('{} plus {} equals {}'.format(x, y, z))

convert={'the_date': 'date'} # convert from amazon type AMAZON.DATE to python type datetime.date
convert={'appointment_time': 'time'} # convert from amazon type AMAZON.TIME to python type datetime.time
convert={'ago': 'timedelta'} # convert from amazon type AMAZON.DURATION to python type datetime.tiemdelta

@ask.intent('AgeIntent', convert={'age': int})
def say_age(age):
    if 'age' in convert_errors:
        # since age failes to convert, it keeps its string
        # value (e.g. "?") for later interrogation
        return question("Can you please repeat your age?")

    # conversion guaranteed to have succeeded
    # age is an int
    return statement("Your age is {}".format(age))

#convert errors is a dict that maps parameter names to the Exceptions raised when writing your own converters
#raise Exceptions on failure, so they work with convert_errors
def to_direction_const(s):
    if s.lower() not in ['left', 'right']:
        raise Exception("must be left or right")
    return LEFT if s == 'left' else RIGHT

@ask.intent('TurnIntent', convert={'direction': to_direction_const})
def turn(direction):
    # do something with direction
    pass

if 'something' in convert_errors:
    pass
if convert_errors:
    pass

@ask.intent('AllYourBaseIntent')
def all_your_base():
    return statement('All your base are belong to us') #statement closes the session after the text has been spoken

@ask.intent('AppointmentIntent')
def make_appointment():
    return question("What day would you like to make an appointemtn for?") #question promps for a response and keeps the session open

@ask.intent('AppontmentIntent')
def make_appointment():
    return question("what day would you like to make and appointment for?") \
        .reprompt("I didn't get that. When would you like to be seen?") #reprompt if the user didnt respond

