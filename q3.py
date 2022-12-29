import re
string = "python_exercises_c#_exercises_django_ _ _ __ exercises"
string2 = ""
for i in string:
    new_string = re.sub(r"_", " ", i)
    new_string2 = re.sub(r"\s", "_", i)
    if i == " ":
        string2 += new_string2
    else:
        string2 += new_string
print(string2)