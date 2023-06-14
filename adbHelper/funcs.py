import matplotlib.pyplot as plt
import csv

## display 3D data (for ACC and GYRO)
def displayData3D(bufferX, bufferY, bufferZ, newData):
    bufferX.extend(newData[0])
    [bufferX.popleft() for i in range(len(newData[0]))]
    bufferY.extend(newData[1])
    [bufferY.popleft() for i in range(len(newData[1]))]
    bufferZ.extend(newData[2])
    [bufferZ.popleft() for i in range(len(newData[2]))]
    plt.clf()
    plt.plot(bufferX, c = 'r')
    plt.plot(bufferY, c = 'g')
    plt.plot(bufferZ, c = 'b')
    plt.pause(0.01)

## display 1D data (for GSR and PPG)
def displayData1D(buffer, newData):
    buffer.extend(newData)
    [buffer.popleft() for i in range(len(newData))]
    plt.clf()
    plt.plot(buffer)
    plt.pause(0.01)

## get new data block from the CSV file
def getNewData(filePath, startRow, sensor):
    sensorFilePath = filePath + "/" + sensor + ".csv"
    newData = []
    with open(sensorFilePath) as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            newRows = reader.line_num
            if reader.line_num > startRow:
                if sensor == 'ACC' or sensor == 'GYRO':
                    if len(row) >= 3:
                        row.pop(0)
                        temp = []
                        for item in row:
                            if item != "":
                                temp.append(float(item))
                        newData.append(temp)
                elif sensor == 'GSR' or sensor == 'PPG':
                    if len(row) >= 2:
                        row.pop(0)
                        if row[0] != "":
                            newData.append(float(row[0]))
        if sensor == 'ACC' or sensor == 'GYRO':
            ## Transpose the new data
            accX = []
            accY = []
            accZ = []
            for data in newData:
                accX.append(data[0])
                accY.append(data[1])
                accZ.append(data[2])
            newDataT = [accX, accY, accZ]
            print(newRows/20)
            return newDataT, newRows
        elif sensor == 'GSR':
            print(newRows/4)
            return newData, newRows
        elif sensor == 'PPG':
            print(newRows/100)
            return newData, newRows
        
