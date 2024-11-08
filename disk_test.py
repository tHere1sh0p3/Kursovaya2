import psutil
import ctypes
import os
from tkinter import *
from tkinter import ttk

def get_volume_label(drive):
    try:
        label = ctypes.create_unicode_buffer(255)
        ctypes.windll.kernel32.GetVolumeInformationW(
            drive,
            label,
            255,
            None,
            None,
            None,
            None,
            None
        )
        return label.value
    except Exception as e:
        return str(e)

def get_usb_drives():
    usb_drives = []
    for part in psutil.disk_partitions():
        if 'removable' in part.opts:
            label = get_volume_label(part.device)
            usage = psutil.disk_usage(part.mountpoint)
            usb_drives.append(f"{label} ({part.mountpoint}) [{usage.total / (1024 ** 3):.1f} ГБ]")
    return usb_drives

if __name__ == "__main__":
    drives = get_usb_drives()
    for drive in drives:
        print(drive)


root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
 

combobox = ttk.Combobox(values=drives)
combobox.pack(anchor=NW, padx=6, pady=6)
 
root.mainloop()