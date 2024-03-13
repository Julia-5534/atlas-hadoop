#!/usr/bin/env python2.7
"""Task 7"""

import sys


top_salaries = []
count = 0

for line in sys.stdin:
    data = line.strip().split('\t')

    if len(data) >= 2:
        id = data[0]
        if id == 'id':
            continue  # Skip the header line
        else:
            key_value_pairs = data[1].split(',')
            company = key_value_pairs[0]
            Salary = float(key_value_pairs[1])

            # Build a 10-element long list
            if count < 10:
                top_salaries.append((id, company, Salary))
                top_salaries.sort(key=lambda x: x[2], reverse=True)
                count += 1
            else:
                top_salaries.append((id, company, Salary))
                top_salaries.sort(key=lambda x: x[2], reverse=True)
                top_salaries.pop()

# Print the top ten salaries
for id, company, Salary in top_salaries:
    print("{}\t{},{}".format(id, company, Salary))
