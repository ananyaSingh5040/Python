def add ():
    """This function performs addition"""
    a=int(input())
    b=int(input())
    addition=a+b
    print(f"{a}+{b}={addition}")
def mult():
    """This function performs multiplication"""
    a=int(input())
    b=int(input())
    multiplication=a*b
    print(f"{a}*{b}={multiplication}")
print(add.__doc__) #SYNTAX FOR DOCSTRING PRINTATION.
add()
print(mult.__doc__)
mult()

