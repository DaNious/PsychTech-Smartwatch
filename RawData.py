import pandas as pd

class RawData:
    def __init__(self):
        # Acc data
        self.accX = []
        self.accY = []
        self.accZ = []
        self.accTime = []
        # Gyro data
        self.gyroX = []
        self.gyroY = []
        self.gyroZ = []
        self.gyroTime = []
        # PPG data
        self.ppgData = []
        self.ppgTime = []
        # GSR data
        self.gsrData = []
        self.gsrTime = []
        # Env data
        self.envData = []
        self.envTime = []

    def addData(self, topic, incData, incTime):
        time = []
        if topic == "raw_acc":
            time.append(incTime)
            for i in range(len(incData[0::3])-1):
                time.append('')
            self.accTime.extend(time)
            self.accX.extend(incData[0::3])
            self.accY.extend(incData[1::3])
            self.accZ.extend(incData[2::3])
        elif topic == "raw_gyro":
            time.append(incTime)
            for i in range(len(incData[0::3])-1):
                time.append('')
            self.gyroTime.extend(time)
            self.gyroX.extend(incData[0::3])
            self.gyroY.extend(incData[1::3])
            self.gyroZ.extend(incData[2::3])
        elif topic == "raw_ppg":
            time.append(incTime)
            for i in range(len(incData)-1):
                time.append('')
            self.ppgTime.extend(time)
            self.ppgData.extend(incData)
        elif topic == "raw_gsr":
            time.append(incTime)
            for i in range(len(incData)-1):
                time.append('')
            self.gsrTime.extend(time)
            self.gsrData.extend(incData)
        elif topic == "raw_env":
            time.append(incTime)
            for i in range(len(incData)-1):
                time.append('')
            self.envTime.extend(time)
            self.envData.extend(incData)
    
    def saveData(self, dir):
        print("Write data to file(s)...")
        accData = [self.accTime, self.accX, self.accY, self.accZ]
        accDf = pd.DataFrame(accData)
        accDf.T.to_csv(dir+"/raw_acc.csv", encoding='utf-8', index=False, header=False)
        gyroData = [self.gyroTime, self.gyroX, self.gyroY, self.gyroZ]
        gyroDf = pd.DataFrame(gyroData)
        gyroDf.T.to_csv(dir+"/raw_gyro.csv", encoding='utf-8', index=False, header=False)
        ppgDataT = [self.ppgTime, self.ppgData]
        ppgDf = pd.DataFrame(ppgDataT)
        ppgDf.T.to_csv(dir+"/raw_ppg.csv", encoding='utf-8', index=False, header=False)
        gsrDataT = [self.gsrTime, self.gsrData]
        gsrDf = pd.DataFrame(gsrDataT)
        gsrDf.T.to_csv(dir+"/raw_gsr.csv", encoding='utf-8', index=False, header=False)
        envDataT = [self.envTime, self.envData]
        envDf = pd.DataFrame(envDataT)
        envDf.T.to_csv(dir+"/raw_env.csv", encoding='utf-8', index=False, header=False)

    def plotData(self):
        ## To-Do
        pass