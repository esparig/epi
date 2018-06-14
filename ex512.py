import random;

def get_sample01(A, s):
    A = random.sample(A, s);
    print(A)

def get_sample02(A, s):
    for i in range(s):
        r = random.randint(0, len(A)-1);
        A[i], A[r] = A[r], A[i]
    print(A[:s])

A = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
get_sample01(A, 3);
get_sample02(A, 3);
