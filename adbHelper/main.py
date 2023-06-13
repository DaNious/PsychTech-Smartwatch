import os
import shutil
import time
from datetime import datetime
from ppadb.client import Client as AdbClient


if(os.path.exists("404971221000")):
    shutil.rmtree("404971221000")
## Check if the device is connected
client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()
if(devices):
    print("ADB device found!")
    dataSavePath = "data/"+datetime.now().strftime("%Y%m%d_%H_%M")
    os.mkdir(dataSavePath)
    while(True):
        os.system('adb pull "/storage/emulated/0/PsychTechFloder/helper/Aiot C1/404971221000"')
        for folder in os.listdir("404971221000"):
            if (not os.listdir("404971221000/"+folder)):
                os.removedirs("404971221000/"+folder)
        shutil.rmtree("404971221000/2022-11-03-17-07-53") # A useless leftover
        temp1 = os.listdir("404971221000")
        if (temp1): # if the data file is successfully pulled from the device
            temp2 = os.listdir("404971221000/" + temp1[0])
            dataPath = "404971221000/" + temp1[0] + '/' + temp2[0] + '/raw'
            shutil.copy(dataPath + "/ACC.csv", dataSavePath + "/ACC.csv")
            shutil.copy(dataPath + "/GSR.csv", dataSavePath + "/GSR.csv")
            shutil.copy(dataPath + "/GYRO.csv", dataSavePath + "/GYRO.csv")
            shutil.copy(dataPath + "/PPG.csv", dataSavePath + "/PPG.csv")
        print("Hold on...")
        time.sleep(3)
else:
    print("No ADB device! Please turn on USB debugging!")
