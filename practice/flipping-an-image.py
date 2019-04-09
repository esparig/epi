import numpy as np
import time

def flip1(A):
    return([[(i==False)&1 for i in row[::-1]] for row in A ])

def flipAndInvertImage(A: 'List[List[int]]') -> 'List[List[int]]':
    l = len(A[0])
    for row in A:
        for i in range(l//2):
            if row[i] == row[l-1-i]:
                row[i] = row[l-1-i] = row[i]^1
        if l & 1 == 1: # odd
            row[l//2] ^= 1
    return A

A = np.random.randint(2, size=(1001, 1001))
start_time = time.time()
B1 = flip1(A)
print("One-liner: ", time.time()-start_time)
start_time = time.time()
B2 = flipAndInvertImage(A)
print("My function: ", time.time()-start_time)
for i in range(len(B1)):
    for j in range(len(B1[0])):
        if B1[i][j] != B2[i][j]:
            print("Diff in ("+str(i)+", "+str(j))
