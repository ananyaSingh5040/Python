#Super Method: used to access methods of parent class.
class Employee:
    company = "Google"
    def __init__(self):
        print("Employee Constructor")
class Coder(Employee):
    name = "Cherry"
    def __init__(self):
        super().__init__()
        print("Coder Constructor")
class Salary(Coder):
    salary = 6000000
    def __init__(self):
        super().__init__()
        print("Salary Constructor")
    def employee(self):
        print(f"{self.name} works in {self.company} and has a salary of {self.salary}")
obj = Salary()
obj.employee()
