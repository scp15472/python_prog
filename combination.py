a=input("Enter first number:")
b=input("Enter second number:")
c=input("Enter third number:")
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            print(d[i],d[j],d[k])
