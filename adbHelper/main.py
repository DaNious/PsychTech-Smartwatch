import os
import shutil
import time
from datetime import datetime
from ppadb.client import Client as AdbClient
import numpy as np
import matplotlib.pyplot as plt
import csv
from collections import deque

# get new data block from the CSV file
def getNewData(filePath, startRow, sensor):
    newData = []
    with open(filePath) as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            newRows = reader.line_num
            if reader.line_num > startRow:
                if len(row) >= 3:
                    row.pop(0)
                    temp = []
                    for item in row:
                        if item != "":
                            temp.append(float(item))
                    newData.append(temp)
        # Transpose the new data
        accX = []
        accY = []
        accZ = []
        for data in newData:
            accX.append(data[0])
            accY.append(data[1])
            accZ.append(data[2])
        newDataT = [accX, accY, accZ]
        return newDataT, newRows

if os.path.exists("404971221000"):
    shutil.rmtree("404971221000")
## Check if the device is connected
client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()
if devices:
    print("ADB device found!")
    dataSavePath = "data/"+datetime.now().strftime("%Y%m%d_%H_%M")
    os.mkdir(dataSavePath)
    newDataRow = 0
    dataDisplayX = deque(np.zeros(200))
    dataDisplayY = deque(np.zeros(200))
    dataDisplayZ = deque(np.zeros(200))
    plt.ion()
    plt.show()
    while True:
        os.system('adb pull "/storage/emulated/0/PsychTechFloder/helper/Aiot C1/404971221000"')
        for folder in os.listdir("404971221000"):
            if (not os.listdir("404971221000/"+folder)):
                os.removedirs("404971221000/"+folder)
        shutil.rmtree("404971221000/2022-11-03-17-07-53") # A useless leftover
        temp1 = os.listdir("404971221000")
        if temp1: # if the data file is successfully pulled from the device, this means the data collection is ongoing
            temp2 = os.listdir("404971221000/" + temp1[0])
            dataPath = "404971221000/" + temp1[0] + '/' + temp2[0] + '/raw'
            pullData, newDataRow = getNewData(dataPath + "/ACC.csv", newDataRow, 'ACC')
            dataDisplayX.extend(pullData[0])
            [dataDisplayX.popleft() for i in range(len(pullData[0]))]
            dataDisplayY.extend(pullData[1])
            [dataDisplayY.popleft() for i in range(len(pullData[1]))]
            dataDisplayZ.extend(pullData[2])
            [dataDisplayZ.popleft() for i in range(len(pullData[2]))]
            plt.clf()
            plt.plot(dataDisplayX, c = 'r')
            plt.plot(dataDisplayY, c = 'g')
            plt.plot(dataDisplayZ, c = 'b')
            plt.pause(0.01)
            ## Copy the data out
            # shutil.copy(dataPath + "/ACC.csv", dataSavePath + "/ACC.csv")
            # shutil.copy(dataPath + "/GSR.csv", dataSavePath + "/GSR.csv")
            # shutil.copy(dataPath + "/GYRO.csv", dataSavePath + "/GYRO.csv")
            # shutil.copy(dataPath + "/PPG.csv", dataSavePath + "/PPG.csv")
        # time.sleep(3)
else:
    print("No ADB device! Please turn on USB debugging!")
