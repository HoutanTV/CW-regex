import re


string = "python exercises 9 00112, c# exercises ,2 django 56 exercises"
matches = re.finditer(r"[0-9]+", string)
# count = len(re.findall(, string))
# print(count)
for match in matches:
    print(f"{match.group()}: {match.start()}")


