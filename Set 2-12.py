my_str = '121'
my_str = my_str.casefold()
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
   print("yes it is palindrome")
else:
   print("no it is palindrome")
