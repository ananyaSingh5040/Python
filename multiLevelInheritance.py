#Multilevel Inheritance
class Employee:
    company = "Google"
    @staticmethod
    def display():
        print("Employee class")
class Coder(Employee):
    name = "Cherry"
    @staticmethod
    def show():
        print("Coder class")
class Salary(Coder):
    salary = 6000000
    def employee(self):
        print(f"{self.name} works in {self.company} and has a salary of {self.salary}")
obj = Coder()
obj.display()
obj.show()

obj = Salary()
obj.display()
obj.show()
obj.employee()
