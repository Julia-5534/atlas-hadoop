#!/usr/bin/env python2.7
"""Task 7"""

import sys


# Initialize an empty array to store top 10 salaries
top_salaries = []

# Read the input from STDIN
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    
    # Split the line into key and value
    key, value = line.split('\t')
    
    # Split the value into company and totalyearlycompensation
    company, totalyearlycompensation = value.split(',')
    
    # Convert totalyearlycompensation to float
    totalyearlycompensation = float(totalyearlycompensation)
    
    # Insert the salary into the top_salaries array
    top_salaries.append((key, company, totalyearlycompensation))
    
    # Sort the top_salaries array in descending order based on totalyearlycompensation
    top_salaries.sort(key=lambda x: x[2], reverse=True)
    
    # Keep only the top 10 salaries
    top_salaries = top_salaries[:10]

# Print the top 10 salaries
for salary in top_salaries:
    key, company, totalyearlycompensation = salary
    print("{}\t{},{}".format(key, company, totalyearlycompensation))
