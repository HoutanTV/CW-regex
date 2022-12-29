import re
string1 = "python exercises , c# exercises Road , django exercises"
def abbreviate(string, pattern):
    matches = re.sub(pattern, f"{pattern[0]}{pattern[-1]}", string)
    return matches
print(abbreviate(string1, "Road"))