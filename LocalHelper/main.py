import paho.mqtt.client as mqtt
import json
import time
import csv
from datetime import datetime
import os
import matplotlib.pyplot as plt

from ServerMsg import ServerMsg
from RawData import RawData
from FeatureData import FeatureData

HOST = '39.107.248.79'

PORT = 1883

rawData = RawData()
featureData = FeatureData()
currentDateTime = datetime.now().strftime("%Y%m%d_%H_%M")
with open("save.sav", "w") as saveFile:
    saveFile.write("data/"+currentDateTime+"/")
if not os.path.exists("data/"+currentDateTime):
    os.makedirs("data/"+currentDateTime)

# On_connect callback
def on_connect(client, userdata, flags, rc):
    print('Connected with result code '+str(rc))
# On_message callback
def on_message(client, userdata, msg):
    serverMsg = ServerMsg(msg.topic, msg.payload)
    topic, data, timeStamp = serverMsg.interpret()
    if data[0] != "":
        if topic[0] == "f": # feature data
            featureData.addFeature(topic, serverMsg.data2float(data), int(timeStamp))
            featureData.saveFeature("data/"+currentDateTime)
        else:   # raw data
            ## save to local variable(s) and plot ##
            rawData.addData(topic, serverMsg.data2float(data), int(timeStamp))
            rawData.saveData("data/"+currentDateTime)
    # rawData.plotData()
    # serverMsg.saveData("data/"+currentDateTime, data)

client = mqtt.Client()

# Assign callback functions
client.on_connect = on_connect
client.on_message = on_message

# Establish connection
client.connect(HOST, PORT, 60)

# Server data (comment as needed)
## Raw data ##
client.subscribe("d/dev-sensing/4049712210/raw/ppg", 0)
client.subscribe("d/dev-sensing/4049712210/raw/gsr", 0)
# client.subscribe("d/dev-sensing/4049712210/raw/acc", 0)
# client.subscribe("d/dev-sensing/4049712210/raw/gyro", 0)
# client.subscribe("d/dev-sensing/4049712210/raw/env", 0)

## Feature data ##
client.subscribe("d/dev-sensing/4049712210/feature/ppg", 0)
client.subscribe("d/dev-sensing/4049712210/feature/gsr", 0)
# client.subscribe("d/dev-sensing/4049712210/feature/acc", 0)
# client.subscribe("d/dev-sensing/4049712210/feature/gyro", 0)

client.loop_forever()