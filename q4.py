import re
url = "https://www.example.com/2022/12/29"
match = re.search(r'([0-9]{4})/([0-9]{2})/([0-9]{2})', url)
year = match.group(1)
month = match.group(2)
day = match.group(3)
print(year) # 2022
print(month) # 12
print(day) # 29