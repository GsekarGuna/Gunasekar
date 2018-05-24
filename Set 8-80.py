n=int(input("Enter number:"))
a=''
while(n!=0):
	t=n%10
	if t%2!=0:
		a=a+' '+str(t)
	n=n//10
print(a[::-1])
