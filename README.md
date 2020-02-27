# RESTful-API

### Write a RESTful service in Python that features the following endpoints.
### GET/fib/<number>: given a number find all  combinations of Fibonacci numbers that add upto that number 
### GET/health: Return health information about the service. 

Wrote python script app.py that you can find attached. I have made use of flask to write the RESTful service with two endpoints. For Fibonacci combinations I have written a recursive function findCombinations() that returns a list of all possible combinations. I used sqlite3 to create a database to log all the requests and responses made. For caching layer I used flask_caching($ pip install flask-caching).

For health information about the service I installed package healthcheck and added a personal check for the health of database in use. Moreover, I have written several tests for the service using unittest in file tests.py.

### Required Packages

```
$ pip install py-healthcheck
```
