i=0

while i<10:
    print("i:",i)
    i += 2

j=1

while(j<1000):
    print("j:",j)
    j *= 2   #j=j*2


k=0

while(k<10):
    if k==5:
        break
    print("k:",k)
    k += 1

m=0

while(m<10):
    if m==3 or m==5:
        i += 1
        continue
    print("m:",m)
    m += 1
 