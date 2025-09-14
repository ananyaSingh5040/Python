class Number:
    def __init__(self,n):
        self.n = n
    def __add__(self, num):
        return f"The addition for the same is : {self.n + num.n}"
num1 = Number(1)
num2 = Number(2)
print(num1 + num2)
