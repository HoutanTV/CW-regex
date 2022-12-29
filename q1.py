import re

def find_substring(pattern,string):
    matches = re.findall(pattern, string)
    return matches

phrase = "python exercises , c# exercises , django exercises"
substring = "exercise"

print(find_substring(substring,phrase))