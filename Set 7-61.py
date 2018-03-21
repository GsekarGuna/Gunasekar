str = input("Enter the string")
n= ''.join([s[:2] for s in str.split(' ')])
print(n)
