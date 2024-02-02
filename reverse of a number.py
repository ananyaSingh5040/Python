rev=0
n=int(input("n: "))
while n!=0:
    a=n%10
    rev=rev*10+a
    n=n//10
print(f"reverse of a number={rev}")
