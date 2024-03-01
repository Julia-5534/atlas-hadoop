#!/usr/bin/env python3
"""Task 4"""

from snakebite.client import Client


def deletedir(l):
    """Deletes Directory"""
    # Create a client
    client = Client('localhost', 9000)

    for dir_path in l:
        # Delete directory in HDFS
        client.rmdir([dir_path])
