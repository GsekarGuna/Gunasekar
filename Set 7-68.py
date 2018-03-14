def isMultipleof7(n):
      
    while ( n > 0 ):
        n = n - 7
  
    if ( n == 0 ):
        return 1
  
    return 0
     
i = 21
if ( isMultipleof7(i) == 1 ):
    print (i, "yes")
else:
    print (i, "no")
