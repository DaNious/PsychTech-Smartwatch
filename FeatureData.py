import pandas as pd

class FeatureData:
    def __init__(self):
        # Acc feature
        self.accFeature = []
        self.accTime = []
        # Gyro feature
        self.gyroFeature = []
        self.gyroTime = []
        # PPG feature
        self.ppgFeature = []
        self.ppgTime = []
        # GSR feature
        self.gsrFeature = []
        self.gsrTime = []

    def addFeature(self, topic, incFeature, incTime):
        if topic == "feature_acc":
            self.accTime.append(incTime)
            self.accFeature.extend(incFeature)
        elif topic == "feature_gyro":
            self.gyroTime.append(incTime)
            self.gyroFeature.extend(incFeature)
        elif topic == "feature_ppg":
            self.ppgTime.append(incTime)
            self.ppgFeature.append(incFeature)
        elif topic == "feature_gsr":
            self.gsrTime.append(incTime)
            self.gsrFeature.append(incFeature)
    
    def saveFeature(self, dir):
        print("Write feature to file(s)...")
        accFeature = [self.accTime, self.accFeature]
        accfDf = pd.DataFrame(accFeature)
        accfDf.T.to_csv(dir+"/feature_acc.csv", encoding='utf-8', index=False, header=False)
        gyroFeature = [self.gyroTime, self.gyroFeature]
        gyrofDf = pd.DataFrame(gyroFeature)
        gyrofDf.T.to_csv(dir+"/feature_gyro.csv", encoding='utf-8', index=False, header=False)
        
        ppgf_Df = pd.concat([pd.DataFrame(self.ppgTime), pd.DataFrame(self.ppgFeature)], axis=1)
        ppgf_Df.to_csv(dir+"/feature_ppg.csv", encoding='utf-8', index=False, header=False)
        gsrf_Df = pd.concat([pd.DataFrame(self.gsrTime), pd.DataFrame(self.gsrFeature)], axis=1)
        gsrf_Df.to_csv(dir+"/feature_gsr.csv", encoding='utf-8', index=False, header=False)
