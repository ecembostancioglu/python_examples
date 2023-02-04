def hi(name):
    print("Hello",name)

hi("Ecem")   #Hello Ecem 
#hi()   #TypeError



def addition(a,b,c):
    print("Total is", a+b+c)

addition(3,4,5)   #Total is 12

list=[1,2,3,4,5,6]
d="car"

print(d.startswith("a"))   #False
print(d.startswith("c"))   #True
print(d.endswith("r"))   #True

d=d.replace("a","o")

print(d)   #cor

list.append("Python")
print(list)   #[1, 2, 3, 4, 5, 6, 'Python']

list.pop(0)
print(list)   #[2, 3, 4, 5, 6, 'Python']
