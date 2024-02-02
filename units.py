a= int(input("Enter the unit: "))
if a>=1 and a<=100:
    print(a*1.5,"is the amount.")
elif a<=200:
    print((100*1.5)+(a-100)*2.5),"is the amount.")
elif a<=300:
    print(100*1.5)+(100*2.5)+(a-200*4) ,"is the amount.")
elif a<=350:
    print((100*1.5)+(100*2.5)+(100*2.5)+(100*4)+(50*5)+(a-350), "is the amount.")
