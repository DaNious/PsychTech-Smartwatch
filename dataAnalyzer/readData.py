# %%
import tkinter as tk
from tkinter.filedialog import askopenfilename
root = tk.Tk()
root.withdraw()
root.call('wm', 'attributes', '.', '-topmost', True)
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import neurokit2 as nk

# %% Read raw data
fs = 4 # sampling rate
dropSec = 20 # drop certain length of data at the beginning
dropSeg = dropSec*fs
filename = askopenfilename(initialdir=os.getcwd()+'/downloads')
df = pd.read_csv(filename)
data = df['data'].dropna().to_numpy()
data = data[dropSeg:]

# %% Plot raw data
# plt.plot(data)
plt.plot(np.linspace(0, len(data)/fs, num=len(data))+dropSeg/fs, data)
plt.xlabel("Time(s)")
plt.show()

# %% PPG signal
ppg = data
ppg_clean = nk.ppg_clean(ppg, sampling_rate=fs, method='elgendi') # cleaning
# ppg_nabian = nk.ppg_clean(ppg, sampling_rate=fs, method='nabian2018', heart_rate=75)
# signals = pd.DataFrame({'PPG_Raw' : ppg,
#                         'PPG_Cleaned' : ppg_clean})
# signals.plot()

peaks = nk.ppg_findpeaks(ppg_clean, sampling_rate=fs, show=False) # find peaks
peaks_index = peaks.get('PPG_Peaks')

# %% 
signals, info = nk.ppg_process(ppg, sampling_rate=fs)
# nk.ppg_plot(signals)
rates = signals.get('PPG_Rate')
plt.plot(np.linspace(0, len(rates)/fs, num=len(rates))+dropSeg/fs, rates)
plt.title("Heart Rate")
plt.xlabel("Time(s)")
plt.show()

# %%
plt.plot(np.linspace(0, len(ppg_clean)/fs, num=len(ppg_clean))+dropSeg/fs, ppg_clean)
plt.plot(peaks_index/fs+dropSeg/fs, ppg_clean[peaks_index], 'o', color = 'red')
plt.show()

# %% GSR signal
gsr = data
signals, info = nk.eda_process(gsr, sampling_rate=4)
nk.eda_plot(signals)

# %%
