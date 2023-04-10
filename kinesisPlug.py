import paho.mqtt.client as mqtt
import json

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
    print(pulseRate,spo2,bpm,glucose,hemoglobin,bodytemp)

client.on_message=notification
client.loop_forever()