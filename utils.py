import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')

def isNumorDot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))

def isValidNumber(string: str):
    valid = True
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid

def isEmpty(string: str):
    return len(string) == 0 