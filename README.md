# PsychTech Smartwatch Local Helper Version 1.0
This is a program used to fetch data recorded by PsychTech smartwatches from **its server**. Afterwards, it can display recorded data and features of last experiment.  
## How to use?
1. Make sure the phone-like assistant and the smartwatch are connected through Bluetooth. (Sometimes you may need to forget the device in the Bluetooth setting and re-connect again.)
2. Wear the smartwatch tightly.
3. Run /LocalHelper/main.py on your desktop.
4. Hit "开始采集" on the assistant to start data collection.
5. When you want to stop the data collection, hit "停止采集" first on the assistant and then press Ctrl + C on your desktop to terminate the program.
6. The data is by default saved to the "/data" folder and you could run dataDisplay.py to check the data of last experiment.

# PsychTech Smartwatch ADB helper
This is a program used to fetch the .csv file recorded by PsychTech smartwatches from **the device itself using ADB**. Afterwards, it can show (update roughly once per second) one of 4 sensors captured data (I didn't have a try to show them all at the same time, but it probably won't perform well due to (1) adb pull takes some file transfer time and (2) python is not efficient enough for real-time processes). 

## How to use?
1. Download "Android SDK Platform Tools" (https://developer.android.com/tools/releases/platform-tools) and then add "adb.exe" to your PATH.
2. Connect the assistant to the desktop through USB and turn on "USB debugging" on the assistant side (https://developer.android.com/studio/debug/dev-options). Then, start the adb daemon by issuing command window "adb start-server" on your desktop. 
3. Make sure that the assistant and smartwatch are connected through Bluetooth.
4. Wear the smartwatch tightly.
5. Edit /adbHelper/main.py to choose which "SENSOR" data you would like to display, and then run the /adbHelper/main.py (optional: comment out "Copy the data out" code section to copy .csv files out)
6. Hit "开始采集" on the assistant to start data collection.
7. When you want to stop the data collection, hit "停止采集" first on the assistant and then press Ctrl + C on your desktop to terminate the program.

# PsychTech Smartwatch Server Data Analyzer
This is to analyze the data downloaded from the cloud server of PsychTech.  

> Cloud server website: https://2in1.psychtech.cn/mgr/index.html

P.S. You must login with your ***account*** and ***password***.