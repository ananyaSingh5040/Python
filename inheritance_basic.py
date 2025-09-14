class Employee:
    def show(self):
        print(f"Hello from Employee Class")
class Programmer(Employee):
    def show1(self):
        print("Hello from Programme Class")
obj = Programmer()
obj.show()
obj.show1()
