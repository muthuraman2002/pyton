

class Vcompany:
    def __init__(self,name,age,id,salary,phone):
        self.name=name
        self.age=age
        self.id=id
        self.salary=salary
        self.phone=phone

    def getEmployeeDetails(self):
        print("name:"+self.name)
        print("Age:",self.age)
        print("ID:",self.id)
        print("Salary:",self.salary)
        print("Phone:",self.phone)

Vcom=Vcompany("MUTHU",25,1001,60000,7200234530)
Vcom.getEmployeeDetails()

