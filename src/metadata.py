from time import *
import os

metadata = {
    "State": "pending", #or "active" or "idle"
    "Title": "Seul la musique",
    "Artist": "unkown",
    "Album": "unkown",
    "Status": "stopped", #or "playing"
    "Position" : "0x00000000 (0)", #(0)in ms
    "Duration": "0x00000000 (0)",
    "TrackNumber": "0x00000000 (0)",
    "NumberOfTracks": "0x00000000 (0)",
    "Volume": "0x0000 (0)"
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
    if line[0:5] == "[CHG]":
        split = str.split()
        key = split[3]
        key = key[0:len(key)-1]

        value = []
        for i in range(0, len(split)-4):
            value.append(split[4+i])
        value = ' '.join(value)

        metadata[key] = value
        return 1
    return 0

file = "/shared/logs/bluetooth.logs"

logfile = open(file, "r")
loglines = follow(logfile)

for line in loglines:
    line_anal(line)
    print(metadata)