import os
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
    for line in lines:
        if (line.find("State") != -1) and (line.find("1") != -1) and logs_init == False:
            # will be done once per session
            txt.close()
            
            #checks pid for if logs.sh is running
            pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]

            for pid in pids:
                try:
                    print(open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()) # print the process name
                    pid_name = open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
                    if pid_name.find("logs.sh") == -1:
                        os.system("./logs.sh")
                except:
                    continue


            logs_init = True
            return 1
        
        if (line.find("Reset") != -1) and (line.find("1") != -1):
            txt.replace("Reset: 1", "Reset: 0")
            txt.close()
            os.system("./restartpair.sh")
            return 1
    txt.close()
    return 0


pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]

for pid in pids:
    try:
        print(open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()) # print the process name
        pid_name = open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
        if pid_name.find("logs.sh") == -1:
            os.system("./logs.sh")
    except:
        continue


while True:
    getData()
    time.sleep(1)