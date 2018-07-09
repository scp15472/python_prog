n=int(input("Enter how any number of element You want: "))
a=[]
for i in range(0,n):
	element=int(input("Enter the Element: "))
	a.append(element)
average=sum(a)/n	
print average


