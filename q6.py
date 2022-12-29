import re
text = ["Power", "Point", "AAAA"]
match = []
for i in text:
    p_word = re.findall(r"^P\w*", i)
    if len(p_word) == 1:
        match.append(p_word[0])
if len(match) == 2:
    print("Match found:", match)
else:
    print("Match not found.")
