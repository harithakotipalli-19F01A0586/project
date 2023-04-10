import dataSource as KinesisDataStream
import paho.mqtt.client as mqtt
import time

kinesisServer='172.31.80.42'
def send_to_kinesisCluster(data):
    client=mqtt.Client()
    client.connect(kinesisServer,1883)
    client.publish('kinesisData',data)
    print('Data Published Successfully')

while True:
    dataStream=KinesisDataStream.data_healthBody()
    send_to_kinesisCluster(dataStream)
    time.sleep(4)