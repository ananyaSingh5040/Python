import re
txt="The rain in spain"
x= re.findall("[arn]", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

txt= "The rain in spain"
x= re.finditer("[a-n]", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
txt= "Before 12:30 PM"
x= re.findall("[a-zA-Z]", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
txt= "The rain in spain"
x= re.findall(r"\bain", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
txt= "The rain in spain"
x= re.findall(r"ain\B")
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

