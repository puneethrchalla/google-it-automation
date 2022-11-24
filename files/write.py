#!/usr/bin/env python3
import os

with open('hello.txt', 'w') as file:
    file.write("hello world, Puneeth!")

os.system("df -h")