class Staff:

    staffCount=0
    raiseRate=1.05

    def __init__(self,name,surname,salary):
        self.name=name
        self.surname=surname
        self.salary=salary
        self.email=f'{name.lower()}.{surname.lower()}@gmx.com'


    def fullName(self):
        return f'{self.name} {self.surname}'
    
    def raiseSalary(self):
     return int(self.salary * self.raiseRate) 
    

    @classmethod 
    def defineNewRaise(cls, rate):
       old_rate=cls.raiseRate
       cls.raiseRate=rate
       print(f'Old rate: {old_rate}, New rate: {cls.raiseRate}')

    @classmethod
    def from_string(cls, per_str):
       name, surname, salary = per_str.split('-')
       return cls(name,surname,salary)
    
    
    @staticmethod 
    def working_day(day): 
        if day.weekday() == 5 or day.weekday() == 6:
          return 'Weekend'
        else:
          return 'Weekday'


per_1=Staff('John','Smith',30000)
per_2=Staff('Mary','Smith',35000)

Staff.defineNewRaise(1.1)

print(Staff.raiseRate)
print(per_1.raiseRate)
print(per_2.raiseRate)

per_str_1='Sam-Winchester-40000'
per_str_2='Dean-Winchester-60000'
per_str_3='Bobby-Winchester-60000'

new_per_1 = Staff.from_string('Sam-Winchester-40000')
print(new_per_1.email)
print(new_per_1.salary)

import datetime

new_date=datetime.date(2023,6,18)
print(new_date.day)
print(Staff.working_day(new_date))


