import re


string = "python exercises , c# exercises , django exercises"
pattern = "exercise"
# Find all occurrences of the pattern in the string
matches = re.finditer(pattern, string)
count = len(re.findall(pattern, string))
# Print the number of matches and the positions of each match
print(count)
for match in matches:
    print(f"Match found at position: {match.start()}")


