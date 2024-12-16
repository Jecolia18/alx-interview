#!/usr/bin/python3
"""utf -8"""


def validUTF8(data):
    """validation of utf8"""
    num_byte = 0

    for i in data:
        byte = i & 0xFF

        if num_byte == 0:
            if (byte >> 7) == 0b0:
                continue
            elif (byte >> 5) == 0b110:
                num_byte = 1
            elif (byte >> 4) == 0b1110:
                num_byte = 2
            elif (byte >> 3) == 0b11110:
                num_byte = 3
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            num_byte = -1
    return num_byte == 0
