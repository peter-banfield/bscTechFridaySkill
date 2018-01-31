from flask import Flask
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def launched():
    return question('Welcome to Calculation! What kind of calculation would you like to preform?')\
        .reprompt('Sorry I missed that. What kind of calculation would you like to do?')

@ask.intent('Addition', convert={'num1': int, 'num2': int})
def addition(num1, num2):
    sum = num1 + num2
    return statement('The sum of {} and {} is {}'.format(num1, num2, sum))

@ask.intent('Subtraction', convert={'num1': int, 'num2': int})
def subtraction(num1, num2):
    difference = num1 - num2
    return statement('The difference between {} and {} is {}'.format(num1, num2, difference))

@ask.intent('Multiplication', convert={'num1': int, 'num2': int})
def multiplication(num1, num2):
    product = num1 * num2
    return statement('The product of {} and {} is {}'.format(num1, num2, product))

@ask.intent('Division')
def division(num1, num2):
    if num2 == 0:
        return statement('Sorry I cannot divide by zero it doesnt make sense.')
    quotient = num1 // num2
    return statement('The quotient of {} and {} is {}'.format(num1, num2, quotient))

@ask.intent('Modulus', convert={'num1': int, 'num2': int})
def modulus(num1, num2):
    if num2 == 0:
        return statement('Sorry I cannot divide by zero it doesnt make sense.')
    remainder = num1 % num2
    return statement('The mod of {} and {} is {}'.format(num1, num2, remainder))

if __name__ == '__main__':
    app.run(debug=True)