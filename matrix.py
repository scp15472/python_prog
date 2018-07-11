import sys
n=int(input("Enter a number: "))
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            sys.stdout.write("1 ")
        else:
            sys.stdout.write("0 ")
    print
