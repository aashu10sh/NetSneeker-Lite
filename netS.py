import sys
import subprocess
import os

try:
    import scapy.all as scapy
except ModuleNotFoundError:
    if sys.platform == "linux":
        subprocess.call(["sudo","pip3","install","scapy"])
    elif sys.platform == "win32":
        subprocess.call(["pip3","install","scapy"])
    elif sys.platform == "mac":
        subprocess.call(["sudo","pip3","install","scapy"])
    else:
        print("Please Make Sure pip3 is installed")

def start():
    print("SYSTEM FOUND ::"+sys.platform)
    choice = input("Enter Range/Netmask> ")
    return choice
    pass


def scan(choice):
    scapy.arping(choice)
    pass

try:
    ip = start()
    scan(ip)
except PermissionError:
    print("Permission Denied, run with sudo")
