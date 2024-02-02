n=int(input("enter the no. of terms:"))
a=0
b=1
counter= 3 #used for third term as the previous two terms are prnted as it is.
sum=0
print(a)
print(b)
while (counter<=n):
 sum= a+b
 print(sum)
 a=b
 b=sum
 counter=counter+1
