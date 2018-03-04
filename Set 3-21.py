def Maximum(arr, low, high):
    max = arr[low]
    i = low
    for i in range(high+1):
        if arr[i] > max:
            max = arr[i]
    return max
arr = [10,20,40,44,90,55,80]
n = len(arr)
print ("The maximum element is %d"%
        Maximum(arr, 0, n-1))
