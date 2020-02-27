

#importing required libraries for the service
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from healthcheck import HealthCheck #installed for health service endpoint
import os
import numpy as np
from flask_caching import Cache

#declaring flask object app
app = Flask(__name__)

#configuring for flask-cache
config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "simple", # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}
app.config.from_mapping(config)
cache = Cache(app)

#setting up the database using flask-sqlalchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir, 'fib2.db') #path for the database
db=SQLAlchemy(app)


class fib_database(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    number = db.Column(db.Integer)
    response = db.Column(db.String)
    def __init__(self, number, response):
        self.number= number
        self.response = response

#calling the HealthCheck package and inserting check for database
health = HealthCheck(app)
def health_database(): #incase /health gives error add self
    is_database_working = True
    output = 'database is ok'
    
    try:
        # to check database we will execute raw query
        db.session.execute('SELECT 1')
    except Exception as e:
        output = str(e)
        is_database_working = False
    return is_database_working, output

health.add_check(health_database)

#fucntion to find the combinations of fibbonaci that add up to number num	
def findCombinationsUtil(arr, index, num, reducedNum, solns): 
    fib =[0]* (num+1)
    fib[1] = 1
    for i in range(2,num+1) : 
        fib[i] = fib[i-1] + fib[i-2] 
    if (reducedNum < 0):
        return solns; 
    sum = 0
    proper_c = list()
    if (reducedNum == 0): 
        for n in arr:
            sum = sum+n
            proper_c.append(n)
            if sum == num:
                break
    	solns.append(proper_c)

    prev = 2 if(index == 0) else arr[index - 1]
  
    solns2 = list()
    for k in range(prev, num + 1): 

        if k in fib:
           arr[index] = k

           solns2 = findCombinationsUtil(arr, index + 1, num, reducedNum - k, solns)#recursion
    return solns2

#endpoint for the fibonacci sequence
@app.route('/fib/<int:number>', methods=['GET']) 
@cache.cached(timeout=50)
def fib(number): 
    arr = [0] * number; 	
    solns = findCombinationsUtil(arr, 0,  number, number, [])
    data=fib_database(number, str(solns)) #assigning data to the database
    db.session.add(data)
    db.session.commit()
    return jsonify(str(solns))

#endpoint for healthcheck
app.add_url_rule("/health", "healthcheck", view_func=lambda: health.run())

#main
if __name__ == '__main__':
    app.run(debug=True)
