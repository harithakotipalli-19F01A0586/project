import paho.mqtt.client as mqtt

kinesisServer='broker.hivemq.com'
client=mqtt.Client()
client.connect(kinesisServer,1883)
print('Connected with Kinesis Server')
client.subscribe('b17/aws')

def notification(client,userdata,msg):
    print(msg.payload)

client.on_message=notification
client.loop_forever()