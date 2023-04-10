import paho.mqtt.client as mqtt
import json
from pymongo import MongoClient as flinkTable
from datetime import datetime

flinkobj=flinkTable('localhost',27017)
db=flinkobj['flink']
c=db['flink table']

kinesisServer='broker.hivemq.com'
client=mqtt.Client()
client.connect(kinesisServer,1883)
print('Connected with Kinesis Server')
client.subscribe('b17/aws')

def notification(client,userdata,msg):
    data=(msg.payload)
    print(data)
    data=data.decode('utf-8')
    data=json.loads(data)
    pulseRate=data['pulseRate']
    spo2=data['spo2']
    bpm=data['bpm']
    glucose=data['glucose']
    hemoglobin=data['hemoglobin']
    bodytemp=data['bodytemp']
    k={}
    k['pulseRate']=pulseRate
    k['spo2']=spo2
    k['bpm']=bpm
    k['glucose']=glucose
    k['hemogloblin']=hemoglobin
    k['bodytemp']=bodytemp
    k['timestamp']=datetime.now()
    c.insert_one(k)
    print(pulseRate,spo2,bpm,glucose,hemoglobin,bodytemp)
    print('Data Stored to Flink Table')

client.on_message=notification
client.loop_forever()