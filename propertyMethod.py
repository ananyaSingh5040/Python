class Employee:
    @property
    def nameFunction(self):
        return f"{self.fname} {self.lname}"
    @nameFunction.setter
    def nameFunction(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
        
obj = Employee()
obj.nameFunction = "Ananya Singh"
print(obj.nameFunction,obj.fname, obj.lname)
