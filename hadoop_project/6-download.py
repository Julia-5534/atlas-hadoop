#!/usr/bin/env python3
"""Task 5"""

from snakebite.client import Client


def download(l):
    """Downloads from HDFS"""
    # Create a client
    client = Client('localhost', 9000)

    for file_path in client.copyToLocal(l, '/tmp'):
        print(file_path)
