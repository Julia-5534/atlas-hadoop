#!/usr/bin/env python3
"""Task 4"""

from snakebite.client import Client


def deletedir(l):
    """Deletes Directory"""
    # Create a client
    client = Client('localhost', 9000)

    try:
        for deleted_dir in client.delete(l, recurse=True):
            print(deleted_dir)
    except Exception:
        pass
