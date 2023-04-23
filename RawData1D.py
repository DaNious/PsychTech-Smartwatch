import matplotlib.pyplot as plt

class RawData1D:
    def __init__(self, modal):
        self.modal = modal
        self.data = []
        plt.ion()
        plt.show()

    def addData(self, incData):
        self.data.extend(incData)
    
    def plotData(self):
        plt.plot(self.data, c = 'r')
        plt.pause(0.05)