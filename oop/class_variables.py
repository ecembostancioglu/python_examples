import math

class Staff:

    raiseRate=1.3

    def __init__(self,name,surname,salary):
        self.name=name
        self.surname=surname
        self.salary=salary
        self.email=f'{name.lower()}.{surname.lower()}@gmx.com'

    def fullName(self):
        return f'{self.name} {self.surname}'
    
    def raiseSalary(self):
      #  return int(self.salary * self.raiseRate) #self.salary=int(self.salary * Staff.raiseRate)
     return int(self.salary * self.raiseRate) #--> 1.5 
    #  return int(self.salary * Staff.raiseRate) --> 1.3
    

per_1=Staff('John','Smith',30000)
per_2=Staff('Mary','Smith',35000)

print(per_1.raiseSalary())

print(Staff.raiseRate)
print(per_1.raiseRate)
print(per_2.raiseRate)

from pprint import pprint

pprint(per_1.__dict__)
per_1.raiseRate=1.5
print('______________After Manipulation______________')
pprint(per_1.__dict__)