n=input("Enter the upper limit for the range:")
l = []
for i in range(0,n+1):
    l.append(str(i))
print '+'.join(l),"=",sum([int(i) for i in l])


