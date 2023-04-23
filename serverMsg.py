class ServerMsg:
    def __init__(self, topic, payload):
        self.topic = topic
        self.payload = payload.decode("utf-8")
    
    def fetchData(self):
        # data are strings between every "[]"
        dataStr = self.payload[self.payload.find("[")+1:self.payload.find("]")]
        dataList = list(dataStr.split(","))
        return dataList
    
    def data2float(self, dataList):
        temp = []
        for data in dataList:
            if data != "":
                temp.append(float(data))
        return temp
    
    def saveData(self, dir, dataList):
        # file name is directory/sensing modality
        with open(dir+"/"+self.topic[self.topic.rfind("/")+1:]+"_data.csv", "a+") as file: 
            for i in range(4):
                print("Write data to file(s)"+"."*i)
            for data in dataList:
                if data != "":
                    file.write(data+",\n")