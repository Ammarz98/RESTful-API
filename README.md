# RESTful-API
# Internship Test for Adnymics
## Task1: Linux:
## Based on history write a bash oneliner to print a count of unique commands that were used in conjunction with sudo.

```bash
$ history|grep sudo|sort|uniq -c
```

## Task2: Python:
### Write a RESTful service in Python that features the following endpoints.
### GET/fib/<number>: given a number find all  combinations of Fibonacci numbers that add unto that number 
### GET/health: Return health information about the service. Definition of »healt check« is up to you.

Wrote python script app.py that you can find attached. I have made use of flask to write the RESTful service with two endpoints. For Fibonacci combinations I have written a recursive function findCombinations() that returns a list of all possible combinations. I have made use of three bonus tasks ( Write tests where it makes sense to you. • Log the requests/responses being made to /fib in a database of your choice. • Caching layer to avoid recalculating of Fibonacci sequences.) to create this service in a manner that they are all linked. I used sqlite3 to create a database to log all the requests and responses made. For caching layer I used flask_caching($ pip install flask-caching).

For health information about the service I installed package healthcheck ($ pip install py-healthcheck) and added a personal check for the health of database in use. Moreover, I have written several tests for the service using unittest in file tests.py.
