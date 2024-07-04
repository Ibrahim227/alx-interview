#!/usr/bin/python3
"""Importing required module/lib"""


def canUnlockAll(boxes):
    """Write a method that determines if all the boxes can be opened"""
    n = 0

    for key in boxes:
        if not isinstance(key, list):
            #n += canUnlockAll(key)
            return True
        else:
            return False
    return
