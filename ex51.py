def dutch_flag(A, p):
    # preparation
    # 1. pivot to last position
    last = len(A)-1;
    aux = A[p];
    A[p] = A[last];
    A[last] = aux;

    # 2. init pointers
    i = 0;
    p1 = p2 = last;
    print(last, p1, p2)

    # 3. go through A
    while i < p1:
        print("i: ",i," p1: ", p1, " A: ",A);
        if A[i] < A[p1]:
            i += 1;

        elif A[i] == A[p1]:
            aux = A[i]; # *
            A[i] = A[p1-1];
            A[p1-1] = A[p1];
            A[p1] = aux; # *
            p1 = p1 - 1;

        else: # A[i] > A[p1]
            aux = A[i];
            A[i] = A[p1-1];
            A[p1-1] = A[p2];
            A[p2] = aux;
            p1 = p1 - 1;
            p2 = p2 - 1;

    return A;

A = [0, 1, 2, 0, 2, 1, 1];
print(A);
dutch_flag(A, 3);
print(A);
