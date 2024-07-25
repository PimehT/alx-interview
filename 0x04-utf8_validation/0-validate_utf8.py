#!/usr/bin/python3
"""Determines if a given data set represents a valid UTF-8 encoding."""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
"""
    following_bytes = 0
    for num in data:
        if following_bytes > 0:    
            if not (num >> 6) == 0b10:
                return False
            following_bytes -= 1
        else:    
            if (num >> 7) == 0:        
                following_bytes = 0
            elif (num >> 5) == 0b110:        
                following_bytes = 1
            elif (num >> 4) == 0b1110:        
                following_bytes = 2
            elif (num >> 3) == 0b11110:        
                following_bytes = 3
            else:        
                return False
    return following_bytes == 0
