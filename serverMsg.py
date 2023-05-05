class ServerMsg:
    def __init__(self, topic, payload):
        self.SN = "4049712210"
        self.topic = topic
        # self.topic = topic[topic.rfind("/")+1:]
        self.payload = payload.decode("utf-8")
    
    def interpret(self):
        # find data with certain pattern
        dataStr = self.payload[self.payload.find("\"data\":[")+8:self.payload.find("]")]
        timeStampStr = self.payload[self.payload.find("\"timestamp\":")+12:self.payload.find("}")]
        topicStr = self.topic[self.topic.find(self.SN)+len(self.SN)+1:]
        dataList = list(dataStr.split(","))
        return topicStr.replace("/", "_"), dataList, timeStampStr
    
    def data2float(self, dataList):
        temp = []
        for data in dataList:
            if data != "":
                temp.append(float(data))
        return temp
    
    def saveData(self, dir, dataList):
        # file name is directory/sensing modality
        with open(dir+"/"+self.topic+"_data.csv", "a+") as file: 
            print("Write "+ self.topic +" data to file(s)...")
            for data in dataList:
                if data != "":
                    file.write(data+",\n")