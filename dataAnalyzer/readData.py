#%%
import tkinter as tk
from tkinter.filedialog import askopenfilename
root = tk.Tk()
root.withdraw()
root.call('wm', 'attributes', '.', '-topmost', True)
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#%%
filename = askopenfilename(initialdir=os.getcwd()+'/downloads')
df = pd.read_csv(filename)
data = df['data'].dropna().to_numpy()

# %%
fs = 100
plt.plot(np.linspace(0, len(data)/fs, num=len(data)), data)
plt.show()
# %%
