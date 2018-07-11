n=input("Enter the upper limit for the range:")
l = []
#	 = 0
for i in range(1,n+1):
#    sum+=i
    l.append(str(i))
 
print '+'.join(l),"=",sum([int(i) for i in l])


'''
(1+2+3+4=10)
'''



    
