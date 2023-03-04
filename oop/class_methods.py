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

print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

class Developer(Staff): #Inheritance
   raiseRate=1.1

   def __init__(self,name,surname,salary,language):
      super().__init__(name,surname,salary)
      self.language=language
      print(f'New staff was moved to Developer class: {self.name} {self.surname}')
      


dev_1=Developer('Dean','Winchester',10000,'python')
dev_2=Developer('Sam','Winchester',15000,'java')

print(dev_1.email)
print(dev_1.salary)
print(dev_1.language)

   
class Manager(Staff):
   
   def __init__(self, name, surname, salary,workers=None):
      super().__init__(name, surname, salary)
      if workers is None:
         self.workers=[]
      else:
         self.workers=workers
        

   def addWorker(self,worke):
    if worke not in self.workers: 
      self.workers.append(worke)

   def deleteWorker(self,worke):
    if worke in self.workers: 
      self.workers.remove(worke)

   
   def listWorkers(self):
     for e, worke in enumerate(self.workers):
        e += 1
        print(e, worke.fullName()) 
 

manager_1=Manager('John','Wick',50000,[dev_1])
manager_2=Manager('John','Snow',50000)

print('_______________________')
manager_1.listWorkers()
print('_______________________')
manager_1.addWorker(dev_2)
manager_1.listWorkers()

#isinstance()

print(isinstance(dev_1,Manager))  #False

print(isinstance(dev_1,Staff))  #True

print(isinstance('EcemB', str))  #True

print(isinstance(35, str))  #False

#issubclass()

print(issubclass(Developer,Staff))  #True

print(issubclass(Manager,Developer))  #False

print(issubclass(Manager,Staff))  #True