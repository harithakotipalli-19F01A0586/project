import paho.mqtt.client as mqtt

kinesisServer='172.31.80.42'
client=mqtt.Client()
client.connect(kinesisServer,1883)
client.subscribe('b17')

def notification(client,userdata,msg):
    print(msg.payload)

client.on_message=notification
client.loop_forever()