import os
import subprocess
import sys
import time

file_data = "/shared/logs/data.log"
logs_init = False

def getData():
    # checks if the button that starts the bluetooth is pressed
    # since the button is handled by another service, we need to check a file from a shared folder that gets updated if the button is pressed

    global logs_init
    if os.path.exists(file_data) == False:
        # if the file doesn't exist, it means that the button has not been/can't be pressed yet
        return -1
    
    txt = open(file_data, "r")
    lines = txt.readlines()

    print(lines) #debug line 

    for line in lines:
        if (line.find("State: 1") != -1) and logs_init == False:
            # will be done once per session
            txt.close()
            
            #checks pid for if logs.sh is running
            pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]

            slip = ''
            for pid in pids:
                try:
                    print(open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()) # print the process name
                    pid_name = open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
                    slip += pid_name
                except:
                    continue
            
            if (slip.find("logs.sh") == -1):
                #starts logs.sh in the background
                #PTN AAAA
                
                cmd = subprocess.Popen("./logs.sh", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                #os.system("bluetoothctl | tee -a /shared/logs/bluetooth.log &")
                logs_init = True
                return 1
        
        if (line.find("Reset: 1") != -1):
            txt.replace("Reset: 1", "Reset: 0")
            txt.close()
            os.system("./restartpair.sh")
            return 1
    txt.close()
    return 0


while True:
    getData()
    time.sleep(1)