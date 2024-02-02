n=int(input("enter number: "))
r=int(input("enter rows: "))
if r>=10 or r<=10:
    for i in range(1,r+1):
        print(n,"*",i,"=",n*i)
    else:
        print("rows exceeded.")
        
