#!/usr/bin/python3
"""Importing required module/lib"""


def canUnlockAll(boxes):
    """Write a method that determines if all the boxes can be opened"""
    boxes = [[]]
    n = 0

    for key in boxes:
        if not isinstance(key, list):
            return
        else:
            n = canUnlockAll(key)
            return True
        return False
