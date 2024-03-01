#!/usr/bin/env python3
"""Task 4"""

from snakebite.client import Client


def createdir(l):
    """Creates Directory"""
    # Create a client
    client = Client('localhost', 9000)

    for dir_path in l:
        # Create directory in HDFS
        client.mkdir([dir_path])
