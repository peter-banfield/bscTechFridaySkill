from flask import Flask
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def launched():
    return question('Welcome to Calculation! What kind of calculation would you like to preform?')\
        .reprompt('Sorry I missed that. What kind of calculation would you like to do?')

@ask.intent('Addition', convert={'first': int, 'second': int})
def addition(first, second):
    sum = first + second
    return statement('The sum of {} and {} is {}'.format(first, second, sum))

@ask.intent('Subtraction', convert={'first': int, 'second': int})
def subtraction(first, second):
    difference = first - second
    return statement('The difference between {} and {} is {}'.format(first, second, difference))

@ask.intent('Multiplication', convert={'first': int, 'second': int})
def multiplication(first, second):
    product = first * second
    return statement('The product of {} and {} is {}'.format(first, second, product))

@ask.intent('Division')
def division(first, second):
    if second == 0:
        return statement('Sorry I cannot divide by zero it doesnt make sense.')
    quotient = first // second
    return statement('The quotient of {} and {} is {}'.format(first, second, quotient))

@ask.intent('Modulus', convert={'first': int, 'second': int})
def modulus(first, second):
    if second == 0:
        return statement('Sorry I cannot divide by zero it doesnt make sense.')
    remainder = first % second
    return statement('The mod of {} and {} is {}'.format(first, second, remainder))

if __name__ == '__main__':
    app.run(debug=True)