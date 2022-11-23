#!/usr/bin/env python3
import csv

hosts = [["home", "192.168.25.68"], ["office", "10.2.5.6"]]

# first, open the file in write mode
with open('hosts.csv', 'w') as csv_write:
    # create the writer object
    writer = csv.writer(csv_write)
    # use writerows() method to write to the file
    writer.writerows(hosts)