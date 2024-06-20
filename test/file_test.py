import os
from db.query import aaa
from test.entity import Person
from datetime import datetime

def ggg():
    print('db.query.aaa=', aaa())

    print('os.getcwd()=',os.getcwd())

    a = Person("a", 12)
    b = Person("b", 22)
 
    aMap = {"1":a, "2":b}

    for k,v in aMap.items():
        print(k, v.name, v.age, v.__dict__)


    

    now = datetime.now() # current date and time
    print(now, now.timestamp(), str(int(now.timestamp())))

    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print("date and time:",date_time)	    


    timestamp = 1528797322
    date_time = datetime.fromtimestamp(timestamp)
    print("Date time object:", date_time)
