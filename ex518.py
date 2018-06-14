def spiral_order(A, n):
    i_ini = 0;
    i_end = n-1;
    j_ini = 0;
    j_end = n-1;
    B = [];
    for step in range(n-1):
        if step%2 == 0:
            B.extend(A[i_ini][j_ini:j_end+1]);
            i_ini += 1;
            for i in range(i_ini, i_end+1):
                B.append(A[i][j_end]);
            j_end -= 1;
        else:
            for j in range(j_end, j_ini-1, -1):
                B.append(A[i_end][j]);
            i_end -= 1;
            for i in range(i_end, i_ini-1, -1):
                B.append(A[i][j_ini]);
            j_ini += 1;
    B.append(A[i_ini][j_ini]);
    return B;

n = 5
A = [[0] * n for i in range(n)]
c = 0;
print("Original:");
for i in range(n):
    for j in range(n):
        A[i][j] = c;
        c += 1;
    print(A[i][:])

print("Result:");
print(spiral_order(A, n));
