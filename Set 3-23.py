def Minimum(arr, low, high):
    min = arr[low]
    i = low
    for i in range(high-1):
        if arr[i] < min:
            min = arr[i]
    return min
arr = [20,40,50,60,1,70]
n = len(arr)
print ("The minimum element is %d"%
        Minimum(arr, 0, n+1))
