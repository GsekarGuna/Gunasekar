num=input("Enter any string:")
n=len(num)
l=list(num)
num=''
if n%2!=0:
	for i in range(n//2):
		num+=l[i]
	num+='*'
	j=n//2+1
else:
  for i in range(n//2):
    num+=l[i]
  num+='*'
  j=n//2+1
for i in range(j,n):
	num+=l[i]
print(num)
