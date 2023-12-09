from flask import Flask, request

app = Flask(__name__)

from operations import add, sub, mult, div

@app.route('/add')
def return_addition():
    """Handle addition from a query string"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(add(a, b))

@app.route('/sub')
def return_subtraction():
    """Handle subtraction from a query string"""
    a = int(request.args["a"])
    b = int(request.args['b'])
    return str(sub(a,b))

@app.route('/mult')
def return_multiplication():
    """Handle multiplication from a query string"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(mult(a,b))

@app.route('/div')
def return_division():
    """Handle division from a query string"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(div(a,b))

OPERATIONS = {'add': add, 'sub': sub, 'mult': mult, 'div': div}

@app.route('/math/<oper>')
def return_arithmetic(oper):
    """Handle arithmetic operations from a query string"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(OPERATIONS[oper](a, b))