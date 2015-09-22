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
    if s == '':
        return False
    if count == None:
        return re.match(r'^(((([A-Za-z]+-)+[A-Za-z]+)|([0-9]+-[A-Za-z]+)|([A-Za-z]+))\s*)*$', s)
    else:
        print(re.split(r'((([A-Za-z]+-)+[A-Za-z]+)|([0-9]+-[A-Za-z]+)|([A-Za-z]+))\s*', s))
        s_split = re.split(r'\s', s)
        if len(s_split) == count and \
           re.match(r'^(((([A-Za-z]+-)+[A-Za-z]+)|([0-9]+-[A-Za-z]+)|([A-Za-z]+))\s*)*$', s):
            return True
        else:
            return False

def phone_number(s):
    return re.match(r'^\(?[0-9]{3}\)?[ .-]?[0-9]{3}[.-]?[0-9]{4}$', s)

def money(s):
    return re.match(r'^\$\d{1,3}([,]?(\d{3}))*([.](\d{2}))?$', s)
















#
