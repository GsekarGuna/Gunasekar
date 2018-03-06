a= int(input("Enter a Number: "))
Sum = 0
while(a> 0):
    Reminder = a% 10
    Sum = Sum + Reminder
    a = a //10
print("\n Sum of the digits= %d" %Sum)
