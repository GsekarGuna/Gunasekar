import math
def perfectsqr(x):
  sr = math.sqrt(x)
  return((sr-math.floor(sr))==0)
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c=a*b
if (perfectsqr(c)):
  print("Yes")
else:
  print("No")
