import matplotlib.pyplot as plt

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
        fig = plt.figure(figsize=(20,10))
        sub1 = fig.add_subplot(511)
        sub2 = fig.add_subplot(512)
        sub3 = fig.add_subplot(513)
        sub4 = fig.add_subplot(514)
        sub5 = fig.add_subplot(515)
        fig.tight_layout()
        sub1.title.set_text("Acc")
        sub2.title.set_text("Gyro")
        sub3.title.set_text("PPG")
        sub4.title.set_text("GSR")
        sub5.title.set_text("Env")
        plt.ion()
        plt.show()

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
        plt.subplot(5, 1, 1)
        plt.plot(self.accX, c = 'r')
        plt.plot(self.accY, c = 'g')
        plt.plot(self.accZ, c = 'b')
        plt.subplot(5, 1, 2)
        plt.plot(self.gyroX, c = 'r')
        plt.plot(self.gyroY, c = 'g')
        plt.plot(self.gyroZ, c = 'b')
        plt.subplot(5, 1, 3)
        plt.plot(self.ppgData, c = 'r')
        plt.subplot(5, 1, 4)
        plt.plot(self.gsrData, c = 'r')
        plt.subplot(5, 1, 5)
        plt.plot(self.envData, c = 'r')
        plt.pause(0.05)