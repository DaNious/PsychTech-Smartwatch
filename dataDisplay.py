import matplotlib.pyplot as plt
import csv

with open("save.sav", "r") as saveFile:
    dataDir = saveFile.read()

# Acc data
accData = []
with open(dataDir+"acc_data.csv", "r") as file:
    for row in csv.reader(file):
        accData.append(float(row[0]))
accX = accData[0::3]
accY = accData[1::3]
accZ = accData[2::3]

# Gyro data
gyroData = []
with open(dataDir+"gyro_data.csv", "r") as file:
    for row in csv.reader(file):
        gyroData.append(float(row[0]))
gyroX = gyroData[0::3]
gyroY = gyroData[1::3]
gyroZ = gyroData[2::3]

# PPG data
ppgData = []
with open(dataDir+"ppg_data.csv", "r") as file:
    for row in csv.reader(file):
        ppgData.append(float(row[0]))

# GSR data
gsrData = []
with open(dataDir+"gsr_data.csv", "r") as file:
    for row in csv.reader(file):
        gsrData.append(float(row[0]))

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