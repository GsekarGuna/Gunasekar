a = 17
b = 27
print("before swapping\na=", a, " b=", b)
a = a ^ b
b = a ^ b
a = a ^ b
print("\nafter swapping\na=", a, " b=", b)
