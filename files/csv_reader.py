#!/usr/bin/env python3
import csv

f = open("airtravel.csv")
csv_f = csv.reader(f)

for row in csv_f:
    print(row)
f.close()
