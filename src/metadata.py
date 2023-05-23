from time import *
import os

metadata = {
    "State": "pending", #or "active" or "idle"
    "Title": "Seul la musique",
    "Artist": "unkown",
    "Album": "unkown", #should not be displayed
    "Status": "stopped", #or "playing"
    "Position" : "0x00000000 (0)", #(0)in ms
    "Duration": "0x00000000 (0)",
    "TrackNumber": "0x00000000 (0)", #should not be displayed
    "NumberOfTracks": "0x00000000 (0)", #should not be displayed
    "Volume": "0x0000 (0)",
    "Device": "unkown"
}

def follow(thefile):
    # source : Generator Tricks For Systems Programmers (V3) by David Beazley
    # http://www.dabeaz.com/generators/Generators.pdf

    # A python version of 'tail -f'
    # Seek to the end of the file and repeatedly try to read new lines. If new data is written to the file, it'll be  picked up.
    thefile.seek(0, os.SEEK_END) #EOF

    while True:
        line = thefile.readline()

        if not line:
            sleep(0.1)
            continue

        yield line

def line_anal(line):
    # this function analyzes the content of each line and
    # uptades the metadata dictionnary according to the current info
    for key in metadata:    # this is not a particularly efficient way to do this, but that's the first thing that came to mind
        index = line.find(key)
        if(index != -1):
            if(line.find("Volume") != -1) or (line.find("Position") != -1) or (line.find("Duration") != -1):
                metadata[key] = line[line.find("(")+1:line.find(")")] #TBD
                print(metadata[key])
                return 1
            metadata[key] = line[index+len(key)+2:-1]
            print(metadata[key])
            return 1
    return 0

file = "/shared/logs/bluetooth.log"

logfile = open(file, "r")
loglines = follow(logfile)

for line in loglines:
    line_anal(line)
    print(metadata)