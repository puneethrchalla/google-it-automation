#!/usr/bin/env python3

from asyncore import write
import csv
atlassian = {"name": "Bamboo", "company": "Atlassian"}
gitlab = {"name": "Gitlab", "company": "Gitlab"}
keys = ["name", "company"]
file = open("citools.csv", "w")
writer = csv.DictWriter(file,fieldnames=keys) # IMPORTANT
writer.writeheader() # IMPORTANT
writer.writerow(atlassian) # IMPORTANT
writer.writerow(gitlab)