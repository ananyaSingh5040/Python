f=open("text file", "r")
print(f.read())

f=open ("text file", "w")
a="hi"
f.write(a)
b=input("enter data:")
f.write(b)
print("data saved in file")
f.close()



f=open("text file", "r+")
f.write("yipeeee!")
print(f.read())
