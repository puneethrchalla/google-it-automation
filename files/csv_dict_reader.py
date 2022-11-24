#!/usr/bin/env python3

import csv

with open('hosts.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print("Host: {}, IP: {}".format(row["host"], row["ip"]))