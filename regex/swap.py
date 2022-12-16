#!/usr/bin/env python3

import re

def name_swap(name):
    pattern = re.search(r"^(\w+)\s?(\w*)\s?(\w?)", name)
    if pattern is None:
        return name
    elif not pattern.group(3) and pattern.group(2):
        return "{} {}".format(pattern.group(2), pattern.group(1))
    elif not pattern.group(3) and not pattern.group(2):
        return pattern.group(1)
    else:
        return "{} {}. {}".format(pattern.group(2), pattern.group(3), pattern.group(1))

print(name_swap("Challa Puneeth Reddy"))