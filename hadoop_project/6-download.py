#!/usr/bin/env python3
"""Task 5"""

from snakebite.client import Client


def download(l):
    """Downloads from HDFS"""
    # Create a client
    client = Client('localhost', 9000)

    for file_path in l:
        # Download file from HDFS to /tmp directory on local system
        with client.read(
            file_path) as reader, open(
                '/tmp/' + file_path.split('/')[-1], 'wb') as writer:
            writer.write(reader.read())
