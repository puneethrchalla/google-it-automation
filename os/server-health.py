#!/usr/bin/env python3
import shutil
import psutil
from network import *

# pass the path on filesystem
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free/du.total * 100
    return free > 20

# checks if CPU Usage is less than 75%
def check_cpu_usage():
    # pass time interval in secs
    usage = psutil.cpu_percent(0.5)
    return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!")
elif check_connectivity() and check_localhost():
    print("Everything is OK!")
else:
    print("Network Error!")