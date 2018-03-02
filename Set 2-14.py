lower=int(input("Enter the First number:"))
upper=int(input("Enter the Second number:"))
for i in range(lower,upper+1):
    if(i%2!=0):
        print(i)
