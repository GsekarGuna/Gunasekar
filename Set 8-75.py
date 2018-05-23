a=input("Enter any string:")
n=len(a)
l=list(a)
a=''
if n%2!=0:
	for i in range(n//2):
		a+=l[i]
	a+='*'
	j=n//2+1
else:
  for i in range(n//2):
    a+=l[i]
  a+='*'
  j=n//2+1
for i in range(j,n):
	a+=l[i]
print(a)
