from flask import Flask
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def launched():
    return question('Welcome to Calculation! What kind of calculation would you like to preform?')\
        .reprompt('Sorry I missed that. What kind of calculation would you like to do?')

@ask.intent('Addition')
def addition(num1, num2):
    sum = num1 + num2
    return statement('The sum of num1 and num2 is sum')

@ask.intent('Subtraction')
def subtraction(num1, num2):
    difference = num1 - num2
    return statement('The difference between num 1 and num2 is difference')

@ask.intent('Multiplication')
def multiplication(num1, num2):
    product = num1 * num2
    return statement('The product of num1 and num2 is product')

@ask.intent('Division')
def division(num1, num2):
    if num2 == 0:
        return statement('Sorry I cannot divide by zero it doesnt make sense.')
    quotient = num1 // num2
    return statement('The quotient of num1 and num2 is quotient')

@ask.intent('Modulous')
def modulous(num1, num2):
    if num2 == 0:
        return statement('Sorry I cannot divide by zero it doesnt make sense.')
    remainder = num1 % num2
    return statement('The mod of num1 and num2 is remainder')

if __name__ == '__main__':
    app.run(debug=True)