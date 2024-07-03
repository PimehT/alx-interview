#!/usr/bin/python3
"""
A method that determines if all the boxes can be opened
"""


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

    keys = set(boxes[0])
    opened = {0}

    next = min(keys - opened)
    while (next < len(boxes)):
        opened.add(next)
        if len(boxes[next]) == 0:
            break
        keys = keys.union(set(boxes[next]))
        if len(keys - opened) == 0:
            break
        next = min(keys - opened)

    return len(opened) == len(boxes)
