a=input("Enter any string:")
lst=list(a)
b=[]
for i in lst:
  if not i in b:
    b.append(i)
if len(b)==len(lst):
  print("Yes")
else:
  print("No")
