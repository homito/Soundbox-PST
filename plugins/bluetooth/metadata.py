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



logfile = open("test.txt", "r")
loglines = follow(logfile)

for line in loglines:
    print(line)



#Agent registered
#AdvertisementMonitor path registered
#[CHG] Transport /org/bluez/hci0/dev_88_46_04_56_33_0A/fd0 State: pending
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Status: stopped
#[CHG] Transport /org/bluez/hci0/dev_88_46_04_56_33_0A/fd0 State: active
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Position: 0x00000000 (0)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Position: 0x00000000 (0)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Status: playing
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Status: stopped
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Title: unknow
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 TrackNumber: 0x00000000 (0)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 NumberOfTracks: 0x00000000 (0)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Duration: 0x00000000 (0)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Album: unknow
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Artist: unknow
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Genre: 
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Position: 0x00000000 (0)
#[CHG] Transport /org/bluez/hci0/dev_88_46_04_56_33_0A/fd0 State: idle
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Position: 0x00000000 (0)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Title: 
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 TrackNumber: 0x00000000 (0)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 NumberOfTracks: 0x00000000 (0)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Duration: 0x00000000 (0)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Artist: 
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Position: 0x00000000 (0)
#[CHG] Transport /org/bluez/hci0/dev_88_46_04_56_33_0A/fd0 State: pending
#[CHG] Transport /org/bluez/hci0/dev_88_46_04_56_33_0A/fd0 State: active
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Title: Why Are Animals Symmetrical?
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 TrackNumber: 0x00000000 (0)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 NumberOfTracks: 0x00000000 (0)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Duration: 0x0008f4f8 (587000)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Artist: 
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Status: playing
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Position: 0x00000000 (0)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Position: 0x00000000 (0)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Status: stopped
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Position: 0x00000000 (0)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Title: unknow
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 TrackNumber: 0x00000000 (0)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 NumberOfTracks: 0x00000000 (0)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Duration: 0x00000000 (0)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Album: unknow
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Artist: unknow
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Genre: 
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Position: 0x00000000 (0)
#[CHG] Transport /org/bluez/hci0/dev_88_46_04_56_33_0A/fd0 State: idle
#[CHG] Transport /org/bluez/hci0/dev_88_46_04_56_33_0A/fd0 State: pending
#[CHG] Transport /org/bluez/hci0/dev_88_46_04_56_33_0A/fd0 State: active
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Title: ZeratoR est dans le Jeux Vidéo Club, de Mario Kart à Warcraft, il nous a TOUT raconté 🔥
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 TrackNumber: 0x00000000 (0)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 NumberOfTracks: 0x00000000 (0)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Duration: 0x001a0428 (1705000)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Artist: 
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Status: paused
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Title: ZeratoR est dans le Jeux Vidéo Club, de Mario Kart à Warcraft, il nous a TOUT raconté 🔥
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 TrackNumber: 0x00000000 (0)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 NumberOfTracks: 0x00000000 (0)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Duration: 0x001a0428 (1705000)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Artist: 
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Position: 0x0000009e (158)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Status: playing
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Position: 0x0000005d (93)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Position: 0x000000eb (235)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Title: ZeratoR est dans le Jeux Vidéo Club, de Mario Kart à Warcraft, il nous a TOUT raconté 🔥
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 TrackNumber: 0x00000000 (0)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 NumberOfTracks: 0x00000000 (0)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Duration: 0x001a0428 (1705000)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Artist: Konbini
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Position: 0x0000022f (559)
#[CHG] Transport /org/bluez/hci0/dev_88_46_04_56_33_0A/fd0 Volume: 0x0059 (89)
#[CHG] Transport /org/bluez/hci0/dev_88_46_04_56_33_0A/fd0 Volume: 0x0061 (97)
#[CHG] Transport /org/bluez/hci0/dev_88_46_04_56_33_0A/fd0 Volume: 0x006a (106)
#[CHG] Transport /org/bluez/hci0/dev_88_46_04_56_33_0A/fd0 Volume: 0x0072 (114)
#[CHG] Transport /org/bluez/hci0/dev_88_46_04_56_33_0A/fd0 Volume: 0x007b (123)
#[CHG] Transport /org/bluez/hci0/dev_88_46_04_56_33_0A/fd0 Volume: 0x0072 (114)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Status: paused
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Position: 0x00002250 (8784)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Status: playing
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Position: 0x0000231c (8988)
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Status: paused
#[CHG] Player /org/bluez/hci0/dev_88_46_04_56_33_0A/player0 Position: 0x00002477 (9335)
#[CHG] Transport /org/bluez/hci0/dev_88_46_04_56_33_0A/fd0 State: idle
#[POCO F3]# exit