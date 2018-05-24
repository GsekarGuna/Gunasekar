s=input("Enter the String:")
result=''
for char in s:
    try:
        number=int(char)
        result=result+char
    except:
        pass
print (result)
