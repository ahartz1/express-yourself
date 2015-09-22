import re


def binary(s):
    return re.match(r'^[01]+$', s)

def binary_even(s):
    return re.match(r'^[01]+0$', s)

def hex(s):
    return re.match(r'^[A-Fa-f0-9]+$', s)

def word(s):
    return re.match(r'^(([A-Za-z]+-)+[A-Za-z]+)|([0-9]+-[A-Za-z]+)|([A-Za-z]+)$', s)

def words(s, count=None):
    if count == None:
        return re.match(r'^((([A-Za-z]+-)+[A-Za-z]+)|([0-9]+-[A-Za-z]+)|([A-Za-z]+)\s*)*$', s)
    else:
        return re.match(r'^((([A-Za-z]+-)+[A-Za-z]+)|([0-9]+-[A-Za-z]+)|([A-Za-z]+)\s*){count}$', s)
