symbols = "~`!@#$%^&*()_-+={}[]:;',.<>/?-+"
n=input("Enter the String:")
count=0
for i in n:
  if i in symbols:
    count+=1
print(count)
