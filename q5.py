import re
calender = "2022-12/29"
match = re.search(r'([0-9]{4})[/-]([0-9]{2})[/-]([0-9]{2})', calender)
result = re.sub(r'([0-9]{4})[/-]([0-9]{2})[/-]([0-9]{2})', f"{match.group(3)}/{match.group(2)}/{match.group(1)}", calender)
print(result)