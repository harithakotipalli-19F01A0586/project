from flask import Flask,render_template,redirect,request
from pymongo import MongoClient as flinkTable

flinkobj=flinkTable('localhost',27017)
db=flinkobj['flink']
c=db['flink table']

app=Flask(__name__)

@app.route('/')
def homePage():
    data=[]
    for i in c.find():
        dummy=[]
        dummy.append(i['pulseRate'])
        dummy.append(i['spo2'])
        dummy.append(i['bpm'])
        dummy.append(i['glucose'])
        dummy.append(i['hemogloblin'])
        dummy.append(i['bodytemp'])
        dummy.append(i['timestamp'])
        data.append(dummy)

    return render_template('index.html',dashboard_data=data,len=len(data))

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)