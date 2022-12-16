#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    for index in range(1,len(sys.argv)):
        print(sys.argv[index])
else:
    print('No args passed!')