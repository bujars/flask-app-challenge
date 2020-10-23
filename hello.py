from flask import Flask, render_template
app = Flask(__name__)

from compute_digit_list import generate_primes_list, non_negative_integer

# Using pagination to request a small number of elements at a time.
from flask_paginate import Pagination, get_page_args



@app.route('/')
def hello_world():
    return "Welcome to flask app challenge!"

def get_digit_list(digit_list, offset=0, per_page=10):
    return digit_list[offset: offset+per_page]

@app.route('/<int(signed=True):number>')
def display_integers_1_to_n(number):
    is_non_negative: bool = non_negative_integer(number)
    if not is_non_negative:
        return render_template("non_negative_integer.html", number=number)
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    numbers: list = list(range(1, number + 1))
    pagination = Pagination(page=page, per_page=per_page, total=len(numbers), css_framework='bootstrap4')
    digit_list = get_digit_list(digit_list=numbers, offset=offset, per_page=per_page)

    return render_template("display_integers.html", title="Display Integers 1 to {}".format(number), numbers=digit_list, page=page, per_page=per_page, pagination=pagination,)

@app.route('/<int(signed=True):number>/even')
def display_evem_integers_to_n(number):
    is_non_negative: bool = non_negative_integer(number)
    if not is_non_negative:
        return render_template("non_negative_integer.html", number=number)
    numbers: list = list(range(2, number+1, 2))
    return render_template("display_integers.html", title="Display Even Integers 2 to {}".format(number), numbers=numbers)



@app.route('/<int(signed=True):number>/odd')
def display_odd_integers_to_n(number):
    is_non_negative: bool = non_negative_integer(number)
    if not is_non_negative:
        return render_template("non_negative_integer.html", number=number)
    numbers: list = list(range(1, number+1, 2))
    return render_template("display_integers.html", title="Display Odd Integers 1 to {}".format(number), numbers=numbers)


@app.route('/<int(signed=True):number>/prime')
def display_prime_integers_to_n(number):
    is_non_negative: bool = non_negative_integer(number)
    if not is_non_negative:
        return render_template("non_negative_integer.html", number=number)
    numbers: list = generate_primes_list(number)
    return render_template("display_integers.html", title="Display Prime Integers 2 to {}".format(number), numbers=numbers)

@app.errorhandler(404)
def not_found(e):
    """Page not found."""
    return render_template("404.html"), 404