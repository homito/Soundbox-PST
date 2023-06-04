#test program
import time
import subprocess
import sys

print("Starting Python service...")
subprocess.Popen(["python3", "metadata.py"])
subprocess.Popen(["python3", "displaydata.py", "--device", "ssh1106"])

while(True):
    time.sleep(1)