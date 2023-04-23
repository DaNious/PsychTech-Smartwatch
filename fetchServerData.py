import paho.mqtt.client as mqtt
import json
import time
import csv
from datetime import datetime
import os

from serverMsg import serverMsg

HOST = '39.107.248.79'

PORT = 1883

# On_connect callback
def on_connect(client, userdata, flags, rc):
    print('Connected with result code '+str(rc))
# On_message callback
def on_message(client, userdata, msg):
    dataMsg = serverMsg(msg.topic, msg.payload)
    data = dataMsg.fetchData()
    # save to a local file
    currentDateTime = datetime.now().strftime("%Y%m%d_%H_%M")
    if not os.path.exists("data/"+currentDateTime):
        os.makedirs("data/"+currentDateTime)
    dataMsg.saveData("data/"+currentDateTime, data)

client = mqtt.Client()

# Assign callback functions
client.on_connect = on_connect
client.on_message = on_message

# Establish connection
client.connect(HOST, PORT, 60)

# Fetch data (comment as needed)
# Raw data
# client.subscribe("d/dev-sensing/4049712210/raw/ppg", 0)
client.subscribe("d/dev-sensing/4049712210/raw/gsr", 0)
# client.subscribe("d/dev-sensing/4049712210/raw/acc", 0)
#client.subscribe("d/dev-sensing/4049712210/raw/gyro", 0)
# client.subscribe("d/dev-sensing/4049712210/raw/env", 0)
# Feature data
# client.subscribe("d/dev-sensing/4049712210/feature/ppg", 0)
# lient.subscribe("d/dev-sensing/4049712210/feature/gsr", 0)
# client.subscribe("d/dev-sensing/4049712210/feature/acc", 0)
# client.subscribe("d/dev-sensing/4049712210/feature/gyro", 0)

client.loop_forever()