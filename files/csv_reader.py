#!/usr/bin/env python3
import csv

file = open("hosts.csv")
csv_f = csv.reader(file)

for row in csv_f:
    host, ip = row
    print("Host: {}, IP: {}".format(host, ip))

file.close()
