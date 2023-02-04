file=open("myfile.txt","w")

file.write("Hello World!")

file.close()

file=open("myfile.txt","a")

file.write("How are you?\n")

file.close()

file=open("myfile.txt","a")

file.write("How old are you?")

file.close()

file=open("myfile.txt","r")

data=file.read(10)
print(data)   #Hello Worl

file.seek(10)
data=file.read(10)
print(data)   #d!How are
