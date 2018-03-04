num = [2, 22, 1, 10,20]
num.sort()
length = len(num)
if (length % 2 == 0):
    median = (num[(length)//2] + num[(length)//2-1]) / 2
else:
    median = num[(length-1)//2]
print(median)
