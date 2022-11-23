#!/usr/bin/env python3
import arrow

# create a date object from a date
date = arrow.get('11-04-1992', 'DD-MM-YYYY')

# format the date 
print(date.shift(weeks=+6).format('MMM DD YYYY'))