#!/usr/bin/env python3

with open('hello.txt') as file:
    print(file.readline()) # reads a single line and leaves file pointer to start of next
    print(file.read()) # reads from current point to end of file