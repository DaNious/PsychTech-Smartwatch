# import matplotlib.pyplot as plt

class RawData:
    def __init__(self):
        self.accData = []
        self.gyroData = []
        self.ppgData = []
        self.gsrData = []
        self.envData = []
        self.accX = []
        self.accY = []
        self.accZ = []
        self.gyroX = []
        self.gyroY = []
        self.gyroZ = []

    def addData(self, modal, incData):
        if modal == "acc":
            self.accData.extend(incData)
            self.accX = self.accData[0::3]
            self.accY = self.accData[1::3]
            self.accZ = self.accData[2::3]
        elif modal == "gyro":
            self.gyroData.extend(incData)
            self.gyroX = self.gyroData[0::3]
            self.gyroY = self.gyroData[1::3]
            self.gyroZ = self.gyroData[2::3]
        elif modal == "ppg":
            self.ppgData.extend(incData)
        elif modal == "gsr":
            self.gsrData.extend(incData)
        elif modal == "env":
            self.envData.extend(incData)
    
    def plotData(self):
        ## To-Do
        pass
