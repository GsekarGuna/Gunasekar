s=input("Enter The string:")
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str
b=reverse(s)
if s==b:
  print("Yes")
else:
  print("No")
