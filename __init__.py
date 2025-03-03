from flask import Flask, render_template, request, redirect, jsonify
from decimal import Decimal

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# Handling Add Request
@app.route('/v1/addition', methods=["POST"])
def add():
    if request.method == "POST":
        num1 = Decimal(request.form['nb_num1'])
        num2 = Decimal(request.form['nb_num2'])
        result = num1 + num2

        responseData = {
            "num1" : num1,
            "num2" : num2,
            "operation": "add",
            "result" : result
        }

        return jsonify(responseData)

# Handling Subtract Request
@app.route('/v1/subtraction', methods=["POST"])
def subtract():
    if request.method == "POST":
        num1 = Decimal(request.form['nb_num1'])
        num2 = Decimal(request.form['nb_num2'])
        result = num1 - num2

        responseData = {
            "num1": num1,
            "num2": num2,
            "operation": "subtract",
            "result": result
        }

        return jsonify(responseData)

if __name__ == '__main__':
    app.run()
