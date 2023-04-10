import dataSource as KinesisDataStream
import paho.mqtt.client as mqtt
import time

kinesisServer='172.31.80.42'
client=mqtt.Client()

def send_to_kinesisCluster(data):
    client.connect(kinesisServer,1883)
    print('Connected with Kinesis Server')
    client.publish('b17/aws',data,0)
    print('Data Published Successfully')
    client.disconnect()

while True:
    dataStream=KinesisDataStream.data_healthBody()
    send_to_kinesisCluster(dataStream)
    time.sleep(4)