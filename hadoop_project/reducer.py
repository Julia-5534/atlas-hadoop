#!/usr/bin/env python3
"""Task 7"""

import sys


def reducer():
    """The Reducer"""
    # Initialize an array to store the top ten salaries
    top_salaries = []

    for line in sys.stdin:
        # Split the line into id, company, and totalyearlycompensation
        id, rest = line.strip().split('\t')
        company, totalyearlycompensation = rest.split(',')

        # Convert totalyearlycompensation to float
        totalyearlycompensation = float(totalyearlycompensation)

        # Add the salary to the top salaries array
        top_salaries.append((totalyearlycompensation, id, company))

        # If the array has more than ten salaries, remove the smallest one
        if len(top_salaries) > 10:
            top_salaries.remove(min(top_salaries))

    # Sort the top salaries array in descending order
    top_salaries.sort(reverse=True)

    # Print the top ten salaries
    for totalyearlycompensation, id, company in top_salaries:
        print(f"{id}\t{company},{totalyearlycompensation}")


if __name__ == "__main__":
    reducer()
