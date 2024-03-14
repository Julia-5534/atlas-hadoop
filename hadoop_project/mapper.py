#!/usr/bin/env python2.7
"""Task 6"""

import csv
import sys


# Create a CSV reader
reader = csv.reader(sys.stdin, delimiter=',')

# Initialize a counter
count = 0

for row in reader:
    # Extract the id, company, and totalyearlycompensation fields
    id = row[0]
    company = row[1]
    totalyearlycompensation = row[3]

    # Print the id, company, and totalyearlycompensation fields
    print("{}\t{},{}".format(id, company,totalyearlycompensation))
