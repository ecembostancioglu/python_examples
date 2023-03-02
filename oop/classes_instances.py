class Staff:
    def __init__(self,name,surname,salary): #Yapıcı fonksiyonu
        #self: sınıftan oluşacak nesneleri ifade eder
        self.name = name.title()
        self.surname = surname.title()
        self.salary = salary
        self.email=f'{name.lower()}.{surname.lower()}@gmx.com'

    def fullName(self):
        return f'{self.name} {self.surname}'
         


per_1 = Staff(name='John',surname='Smith', salary=30000)
per_2 = Staff('Mary','Smith',35000)

print(per_1.name) #John
print(per_1.surname) #Smith
print(per_1.salary) #30000
print(per_1.email) #john.smith@gmx.com


print(f'{per_2.name} {per_2.surname}') #Mary Smith

print('{} {}'.format(per_2.name,per_2.surname)) #Mary Smith

print('****************************************')

print(per_1.fullName()) #John Smith

print(Staff.fullName(per_1)) #John Smith