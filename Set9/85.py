a=input("Enter the string:")
l=list(a)
even=''
odd=''
for i in range(len(l)):
  if i%2==0:
    even=even+l[i]
  else:
    odd=odd+l[i]
print(even)
print(odd) 
