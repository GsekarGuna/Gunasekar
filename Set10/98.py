n=int(input("Enter the Range:"))
l=[]
for i in range(n):
	l.append(int(input("Enter the Value:")))
for i in range(1,n):
	if l[i-1]>l[i]:
		print(l[i-1])
		
