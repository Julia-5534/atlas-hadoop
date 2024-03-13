#!/usr/bin/env python3
"""Task 3"""

from snakebite.client import Client


def createdir(l):
    """Creates Directory"""
    # Create a client
    client = Client('localhost', 9000)

    for created_dir in client.mkdir(l, create_parent=True):
        print(created_dir)
