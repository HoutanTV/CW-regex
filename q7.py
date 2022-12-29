import re
def counter_num(string):
    result = ""
    for i in string:
        char = re.findall(r"[0-9]", i)
    if len(char) > 0:
        result += char[0]
    return result
print(counter_num("1212312fws fndisuafhqo`ou213gb1iy2341"))
