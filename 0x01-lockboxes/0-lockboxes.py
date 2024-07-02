#!/usr/bin/python3
"""
A method that determines if all the boxes can be opened
"""
from collections import deque

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened
    Args:
    boxes(list) - a list of lists
    Returns:
    True - if the keys can all the boxes
    Otherwise False
    """
    if len(boxes) == 0:
        return False

    opened = set()
    to_open = [0]

    while to_open:
        current = to_open.pop(0)
        if current not in opened:
            opened.add(current)
            for key in boxes[current]:
                if key not in opened and key < len(boxes):
                    to_open.append(key)

    return len(opened) == len(boxes)
