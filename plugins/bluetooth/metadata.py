import dbus

with open("test.txt", "r") as f:
    line = f.readline()
    parts = line.split(":")
    bus_name = parts[0]
    object_name = parts[1]

bus_name = ""
object_name = ""

bus = dbus.SystemBus()
obj = bus.get_object('org.bluez', '/org/bluez/hci0/dev_XX_XX_XX_XX_XX_XX/player0')
iface = dbus.Interface(obj, 'org.bluez.MediaPlayer1')
metadata = iface.Get('org.bluez.MediaPlayer1', 'Metadata')
print(metadata)