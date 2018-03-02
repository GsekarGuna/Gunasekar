lower_limit = int(input("Enter the first number:"))
upper_limit = int(input("Enter the second number:"))
for i in range(lower_limit,upper_limit+1):
  if(i%2 == 0):
    print(i)
