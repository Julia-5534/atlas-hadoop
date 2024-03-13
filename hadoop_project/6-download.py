#!/usr/bin/env python3
"""Task 5"""

from snakebite.client import Client


def download(l):
    """Downloads from HDFS"""
    # Create a client
    client = Client('localhost', 9000)

    try:
        for file_path in l:
            # Open the file in HDFS for reading
            with client.open(file_path) as reader:
                # Read the data and write it to a local file
                with open('/tmp/' + file_path.split('/')[-1], 'wb') as writer:
                    writer.write(reader.read())
    except Exception:
        pass
