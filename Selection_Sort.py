# Write a Python program to implement Selection sort :: Advance Algorithm Assignment 1 :: MD RASIDUL ISLAM

import sys
A = [64, 25, 12, 22, 11]

for i in range(len(A)):
  min_idx = i
  for j in range(i+1, len(A)): 
    if A[min_idx] > A[j]: 
        min_idx = j 
        A[i], A[min_idx] = A[min_idx], A[i] 
        print ("Selection Sorted Array") 
        for i in range(len(A)): 
            print("%d" %A[i])
