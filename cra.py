import re
txt = "The rain in Spain"
x= re.findall("[a-m]", txt)
print(x)

txt= "That will be 59 dollars"
x= re.findall("/d", txt)
print(x)

txt="hello planet helo helo he@o"
x= re.findall("he..o", txt)
print(x)

