import os
import shutil
import time
from datetime import datetime
from ppadb.client import Client as AdbClient
import numpy as np
import matplotlib.pyplot as plt
import csv
from collections import deque
from funcs import getNewData, displayData1D, displayData3D

SENSOR = "GSR" # Select which sensor to be displayed (options: 'ACC', 'GYRO', 'PPG', 'GSR')

if SENSOR == 'ACC' or SENSOR == 'GYRO':
    dataDisplayX = deque(np.zeros(200))
    dataDisplayY = deque(np.zeros(200))
    dataDisplayZ = deque(np.zeros(200))
elif SENSOR == 'PPG':
    dataDisplay1k = deque(np.zeros(1000))
elif SENSOR == 'GSR':
    dataDisplay100 = deque(np.zeros(100))

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
    plt.ion()
    plt.show()
    while True:
        os.system('adb pull "/storage/emulated/0/PsychTechFloder/helper/Aiot C1/404971221000"')
        for folder in os.listdir("404971221000"):
            if (not os.listdir("404971221000/"+folder)):
                os.removedirs("404971221000/"+folder)
        if os.path.exists("404971221000/2022-11-03-17-07-53"): # A useless leftover
            shutil.rmtree("404971221000/2022-11-03-17-07-53") 
        temp1 = os.listdir("404971221000")
        ## if the data file is successfully pulled from the device, this means the data collection is ongoing
        if temp1: 
            temp2 = os.listdir("404971221000/" + temp1[0])
            dataPath = "404971221000/" + temp1[0] + '/' + temp2[0] + '/raw'
            ## get new data from the pulled file
            pullData, newDataRow = getNewData(dataPath, newDataRow, SENSOR)
            ## Show data
            if SENSOR == 'ACC' or SENSOR == 'GYRO':
                ## Display 3D data
                displayData3D(dataDisplayX, dataDisplayY, dataDisplayZ, pullData)
            elif SENSOR == 'PPG':
                ## Display 1D data
                displayData1D(dataDisplay1k, pullData)
            elif SENSOR == 'GSR':
                ## Display 1D data
                displayData1D(dataDisplay100, pullData)
            ## Copy the data out
            # shutil.copy(dataPath + "/ACC.csv", dataSavePath + "/ACC.csv")
            # shutil.copy(dataPath + "/GSR.csv", dataSavePath + "/GSR.csv")
            # shutil.copy(dataPath + "/GYRO.csv", dataSavePath + "/GYRO.csv")
            # shutil.copy(dataPath + "/PPG.csv", dataSavePath + "/PPG.csv")
else:
    print("No ADB device! Please turn on USB debugging!")