digit = int(input("Please Enter any Number: "))
Reverse = 0
while(digit > 0):
    Reminder = digit %10
    Reverse = (Reverse *10) + Reminder
    digit = digit //10
 
print Reverse
