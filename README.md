# flask-app-challenge

## How to Clone and Run 
1. Clone the repo
2. cd flask-app-challenge
3. python3 -m venv venv
4. . venv/bin/activate
5. pip install flask
6. export FLASK_APP=hello.py
7. flask run

## To run with dockerfile:
8. sudo docker build --tag flask-app-challenge .
9. sudo docker run --name flask-app-challenge -p 5001:5001 flask-app-challenge

## Current Endpoints: 
1. /<int:number> will display integers from 1 to that number
2. /<int:number>/odd will display only odd numbers in that range
3. /<int:number>/even will display only even numbers in that range
4. /<int:number>/prime will display only prime numbers in that range

## Current Bugs/Things to do:
- simplify routes to one function that differs in / /even /odd /prime
(ie one function to handle all four cases, and manipulate numbers list and title)
        so that we aren't copying over code multiple times (simple to do)
- Add a proper response page for 400 (bad request error)
- Add unit test cases
- For integer, check the upperbound (or provide an upper bound)
- Rewrite your own Pagination, or manipulate the pagination to create the list on interval
(Started doing this but ran out of time -- backtrack commit if needed)
(Current pagination depends on the list existing -- for page numbers)
- getting an interval for even/odd/normal is simple, but we would need a way for primes!