#!/usr/bin/env python3

with open('hello.txt') as file:
    for line in file:
        print(line.strip().upper())

file = open('hello.txt')
content = file.readlines() # convert file content to a list
print(content)
file.close

# don't read large files into memory