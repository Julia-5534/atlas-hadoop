#!/usr/bin/env python3
"""Task 6"""

import sys
import csv


def mapper():
    """The Mapper"""
    # Create a CSV reader
    reader = csv.reader(sys.stdin)

    # Skip the header row
    next(reader, None)

    for row in reader:
        # Extract the id, company, and totalyearlycompensation fields
        id = row[0]
        company = row[1]
        totalyearlycompensation = row[2]

        # Print the id, company, and totalyearlycompensation fields
        print(f"{id}\t{company},{totalyearlycompensation}")
