import cmath

def quadratic(a,b,c):
	d=(b**2)-(4*a*c)
	sol1 = (-b-cmath.sqrt(d))/(2*a)
	sol2 = (-b+cmath.sqrt(d))/(2*a)
	return sol1,sol2
 	

print quadratic(1,3,-4)
