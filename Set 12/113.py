num=int(input("Enter N number:"))
k=int(input("Enter K value:"))
b=[]
c=0
for i in range(0,num):
  a=int(input())
  b.append(a)
for i in b:
  if k==i:
    c+=1
print(c)
