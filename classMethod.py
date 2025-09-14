#Class Method
class Employee:
    name = "Cherry"
    @classmethod
    def show(cls):
        print(f"Class Attribute is : {cls.name}")
obj = Employee()
obj.name = "Aaloo"
obj.show()
