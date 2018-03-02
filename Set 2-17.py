n=int(input("Enter any number: "))
a=list(map(int,str(n)))
b=list(map(lambda x:x**3,a))
if(sum(b)==n):
    print("Yes it an arsmtrong number.")
else:
    print("No it is arsmtrong number.")
