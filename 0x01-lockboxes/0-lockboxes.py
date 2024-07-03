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
    if not boxes:
        return False

    n = len(boxes)
    opened = set()
    stack = [0]

    while stack:
        current_box = stack.pop()
        if current_box not in opened:
            opened.add(current_box)
            for key in boxes[current_box]:
                if key < n:
                    stack.append(key)

    return len(opened) == n
