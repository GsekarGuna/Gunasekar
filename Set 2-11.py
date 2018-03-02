def power(base,pow):
    if(pow==1):
        return(base)
    if(pow!=1):
        return(base*power(base,pow-1))
base=int(input("Enter base: "))
pow=int(input("Enter power value: "))
print("Result:",power(base,pow))
