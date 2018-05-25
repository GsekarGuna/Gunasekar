a=int(input("Enter n value:"))
b=int(input("Enter k value:"))
l=[]
for i in range(0,a):
  l.append(int(input()))
l.sort()
print(l[b-1])
