l=int(input("Enter the 1 range:"))
r=int(input("Enter the 2 range:"))
c=0
for i in range(l,r + 1):
   if  i> 1:
       for j in range(2,i):
           if (i%j) == 0:
               break
       else:
           c+=1
print(c)
