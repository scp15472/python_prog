lower=input("Enter lower range limit:")
upper=input("Enter upper range limit:")
n=input("Enter the number to be divided by:")
for i in range(lower,upper+1):
    if(i%n==0):
        print(i)
