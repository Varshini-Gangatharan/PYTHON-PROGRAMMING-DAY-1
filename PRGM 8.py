import re
def is_valid_number(s):
    pattern = r'^[+-]?(\d+\.\d*|\.\d+|\d+)([eE][+-]?\d+)?$'
    match = re.match(pattern, s)
    return match is not None
print(is_valid_number("0"))
