import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
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

# Acc feature
headers = ['Timestamp', 'Feature']
df = pd.read_csv(dataDir+'feature_acc.csv', names=headers)
accFTime = df['Timestamp'].to_list()
accFTime = [x - accFTime[0] for x in accFTime]
accFeature = df['Feature'].to_list()

# Gyro feature
headers = ['Timestamp', 'Feature']
df = pd.read_csv(dataDir+'feature_gyro.csv', names=headers)
gyroFTime = df['Timestamp'].to_list()
gyroFTime = [x - gyroFTime[0] for x in gyroFTime]
gyroFeature = df['Feature'].to_list()


# ppg feature

# features = ['mean_T1', 'std_T1', 'mean_T2',	'std_T2',
#             'mean_T', 'std_T', 'mean_RTR', 'std_RTR', 'mean_A1', 
#             'std_A1', 'mean_A2', 'std_A2', 'mean_A', 'std_A',
#             'mean_RAR', 'std_RAR', 'mean_H1', 'std_H1', 'mean_H2',
#             'std_H2', 'mean_RPR', 'std_RPR', 'IBI_PPG', 'SDNN_PPG',
#             'HR_PPG', 'RMSSD_PPG', 'N20_PPG', 'pN20_PPG', 'N50_PPG',
#             'pN50_PPG', 'mean_PPG',	'std_PPG', 'energy_PPG', 
#             'time_duration', 'Bandwidth', 'TBP', 'Dimensionality',
#             'LF_PPG', 'HF_PPG',	'TF_PPG', 'PoB_PPG', 'LHR_PPG',	'Resp', 'Quality_Peak']
ppgHeaders = ['Timestamp']
for i in range(45):
    ppgHeaders.append('ppg_feature_'+str(i+1))

df = pd.read_csv(dataDir+'feature_ppg.csv', names=ppgHeaders)
ppgFTime = df['Timestamp'].to_list()
ppgFTime = [x - ppgFTime[0] for x in ppgFTime]
ppgFeature = df.iloc[:,1:].T.values.tolist()

# gsr feature
# features = ['mean_SCR', 'med_SCR', 'std_SCR', 'var_SCR', 'min_SCR',
#             'max_SCR', 'mean_SCL', 'med_SCL', 'std_SCL', 'var_SCL',	
#             'min_SCL', 'max_SCL', 'mean_GSR', 'med_GSR', 'std_GSR',	
#             'var_GSR', 'min_GSR', 'max_GSR', 'mean_diff1', 'med_diff1',	
#             'std_diff1', 'var_diff1', 'min_diff1', 'max_diff1', 'mean_diff2',
#             'med_diff2', 'std_diff2', 'var_diff2', 'min_diff2',	
#             'max_diff2', 'mean_der1', 'med_der1', 'std_der1', 
#             'var_der1', 'min_der1', 'max_der1', 'mean_der2', 'med_der2',
#             'std_der2',	'var_der2',	'min_der2',	'max_der2', 'LF_GSR',
#             'HF_GSR', 'Symp_GSR', 'LHR_GSR', 'num_SCR', 'ristime_SCR',
#             'amp_SCR', 'area_SCR', 'Quality_GSR']
gsrHeaders = ['Timestamp']
for i in range(51):
    gsrHeaders.append('gsr_feature_'+str(i+1))

df = pd.read_csv(dataDir+'feature_gsr.csv', names=gsrHeaders)
gsrFTime = df['Timestamp'].to_list()
gsrFTime = [x - gsrFTime[0] for x in gsrFTime]
gsrFeature = df.iloc[:,1:].T.values.tolist()

## Plot ##
# plot acc data
# fig = plt.figure()
# plt.plot(np.linspace(0, len(accX)/20, num=len(accX)), accX, c = 'r', label="accX")
# plt.plot(np.linspace(0, len(accY)/20, num=len(accY)), accY, c = 'g', label="accY")
# plt.plot(np.linspace(0, len(accZ)/20, num=len(accZ)), accZ, c = 'b', label="accZ")
# plt.legend(loc="lower right")
# plt.title("Accelerometer Readings")
# plt.xlabel("Time(s)")

# plot ppg and gsr data
fig = plt.figure(figsize=(20,10))
sub1 = fig.add_subplot(211)
plt.plot(np.linspace(0, len(ppgData)/100, num=len(ppgData)), ppgData)
plt.xlabel("Time(s)")
sub2 = fig.add_subplot(212)
plt.plot(np.linspace(0, len(gsrData)/4, num=len(gsrData)), gsrData)
plt.xlabel("Time(s)")
sub1.title.set_text("PPG raw signal")
sub2.title.set_text("GSR raw signal")
fig.tight_layout()

# plot ppg features
fig = plt.figure(figsize=(20,10))
plt.suptitle("PPG features")
for i in range(len(ppgFeature)):
    sub = fig.add_subplot(5,9,i+1)
    sub.title.set_text(ppgHeaders[i+1])
    plt.plot([x/1000 for x in ppgFTime], ppgFeature[i])
    plt.xlabel("Time(s)")
fig.tight_layout()

# plot gsr features
fig = plt.figure(figsize=(20,10))
plt.suptitle("GSR features")
for i in range(len(gsrFeature)):
    sub = fig.add_subplot(6,9,i+1)
    sub.title.set_text(gsrHeaders[i+1])
    plt.plot([x/1000 for x in gsrFTime], gsrFeature[i])
    plt.xlabel("Time(s)")
fig.tight_layout()

plt.show()