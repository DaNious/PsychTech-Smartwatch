import matplotlib.pyplot as plt
import csv

with open("save.sav", "r") as saveFile:
    dataDir = saveFile.read()

# Acc data
accX = []
accY = []
accZ = []
with open(dataDir+"raw_acc.csv", "r") as file:
    for col in csv.reader(file):
        accX.append(float(col[1]))
        accY.append(float(col[2]))
        accZ.append(float(col[3]))

# Gyro data
gyroX = []
gyroY = []
gyroZ = []
with open(dataDir+"raw_gyro.csv", "r") as file:
    for col in csv.reader(file):
        gyroX.append(float(col[1]))
        gyroY.append(float(col[2]))
        gyroZ.append(float(col[3]))

# PPG data
ppgData = []
with open(dataDir+"raw_ppg.csv", "r") as file:
    for col in csv.reader(file):
        ppgData.append(float(col[1]))

# GSR data
gsrData = []
with open(dataDir+"raw_gsr.csv", "r") as file:
    for col in csv.reader(file):
        gsrData.append(float(col[1]))

fig = plt.figure(figsize=(20,10))
sub1 = fig.add_subplot(411)
sub2 = fig.add_subplot(412)
sub3 = fig.add_subplot(413)
sub4 = fig.add_subplot(414)
fig.tight_layout()
sub1.title.set_text("Acc")
sub2.title.set_text("Gyro")
sub3.title.set_text("PPG")
sub4.title.set_text("GSR")

plt.subplot(4, 1, 1)
plt.plot(accX, c = 'r')
plt.plot(accY, c = 'g')
plt.plot(accZ, c = 'b')
plt.subplot(4, 1, 2)
plt.plot(gyroX, c = 'r')
plt.plot(gyroY, c = 'g')
plt.plot(gyroZ, c = 'b')
plt.subplot(4, 1, 3)
plt.plot(ppgData, c = 'r')
plt.subplot(4, 1, 4)
plt.plot(gsrData, c = 'r')
plt.show()