import random

def data_healthBody():
    pulseRate=random.randint(60,100)
    spo2=random.randint(80,100)
    bpm=random.randint(80,120)
    glucose=random.randint(140,250)
    hemoglobin=random.randint(5,8)
    bodytemp=random.randint(90,110)
    dataStream='{"pulseRate": ' +str(pulseRate)+ ',"spo2": '+str(spo2)+',"bpm": '+str(bpm)+',"glucose": '+str(glucose)+',"hemoglobin": '+str(hemoglobin)+',"bodytemp": '+str(bodytemp)+'}'
    print(dataStream)
    return dataStream
