import re

def solution(s):
    parts = re.split(r'(\s+)', s)
    result = []
    for part in parts:
        if part.strip():
            if not part[0].isdigit():
                result.append(part[0].upper() + part[1:].lower())
            else:
                result.append(part[0] + part[1:].lower())
        else: 
            result.append(part)
    return ''.join(result)