import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib

# Initialize the D-Bus main loop
DBusGMainLoop(set_as_default=True)

# Create a session bus connection
bus = dbus.SystemBus()

# Get the Bluetooth adapter object path
manager_obj = bus.get_object('org.bluez', '/')
manager_iface = dbus.Interface(manager_obj, 'org.freedesktop.DBus.ObjectManager')
objects = manager_iface.GetManagedObjects()

adapter_path = None
for path, interfaces in objects.items():
    if 'org.bluez.Adapter1' in interfaces:
        adapter_path = path
        break

if adapter_path is None:
    print("No Bluetooth adapter found.")
    exit(1)

# Create a proxy object for the adapter
adapter_obj = bus.get_object('org.bluez', adapter_path)
adapter_iface = dbus.Interface(adapter_obj, 'org.freedesktop.DBus.Properties')

# Check if any devices are connected
properties = adapter_iface.GetAll('org.bluez.Adapter1')
is_connected = properties['Connected']

if is_connected:
    print("Bluetooth device(s) connected.")
else:
    print("No Bluetooth device(s) connected.")
