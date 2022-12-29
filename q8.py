import re

text = "mmd are akbar ekbatan nayoomade narafte ab bazi"

resault = re.findall(r"[ae]\w*",text)
print(resault)