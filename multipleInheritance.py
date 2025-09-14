class Employee:
    company = "Google"
    @staticmethod
    def display():
        print("Employee class")
class Coder:
    name = "Cherry"
    @staticmethod
    def show():
        print("Coder class")
class Salary(Employee, Coder):
    salary = 6000000
    def employee(self):
        print(f"{self.name} works in {self.company} and has a salary of {self.salary}")
obj = Salary()
# obj.show()
# obj.display()
obj.employee()
