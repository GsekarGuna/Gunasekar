num=int(input("Enter the number:"))
l=[]
b=[]
set=0
for i in range(0,num):
  a=int(input())
  l.append(a)
l.sort()
c=len(l)
for i in range(1,c):
	if l[i]==l[i-1] :
		if l[i] in b :
			set=1
		b.append(l[i])
if set==0:
  print ("Unique")
