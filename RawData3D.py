import matplotlib.pyplot as plt

class RawData3D:
    def __init__(self, modal):
        self.modal = modal
        self.data = []
        plt.ion()
        plt.show()

    def addData(self, incData):
        self.data.extend(incData)
        self.x = self.data[0::3]
        self.y = self.data[1::3]
        self.z = self.data[2::3]
    
    def plotData(self):
        plt.plot(self.x, c = 'r')
        plt.plot(self.y, c = 'g')
        plt.plot(self.z, c = 'b')
        plt.pause(0.05)