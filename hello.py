from flask import Flask, render_template
app = Flask(__name__)

from compute_digit_list import generate_primes_list

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/<int:number>')
def display_integers_1_to_n(number):
    numbers: list = list(range(1, number+1))
    return render_template("display_integers.html", title="Display Integers 1 to {}".format(number), numbers=numbers)

@app.route('/even/<int:number>')
def display_evem_integers_to_n(number):
    numbers: list = list(range(2, number+1, 2))
    return render_template("display_integers.html", title="Display Even Integers 2 to {}".format(number), numbers=numbers)


@app.route('/odd/<int:number>')
def display_odd_integers_to_n(number):
    numbers: list = list(range(1, number+1, 2))
    return render_template("display_integers.html", title="Display Odd Integers 1 to {}".format(number), numbers=numbers)


@app.route('/prime/<int:number>')
def display_prime_integers_to_n(number):
    numbers: list = generate_primes_list(number)
    return render_template("display_integers.html", title="Display Prime Integers 2 to {}".format(number), numbers=numbers)