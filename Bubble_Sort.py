# Write a Python program to implement Bubble sort :: Advance Algorithm Assignment :: MD RASIDUL ISLAM

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)
print ("Bubble Sorted Array is:")
for i in range(len(arr)):
    print ("% d" % arr[i],end=" ")
