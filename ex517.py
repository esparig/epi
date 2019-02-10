def sudoku_checker(A):
    def check_region(s_row, e_row, s_col, e_col, A):
        nums = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(s_row, e_row+1):
            for j in range(s_col, e_col+1):
                cur = A[i][j]
                if cur != 0:
                    if nums[cur-1] > 0:
                        print(cur, i,j)
                        return False
                    nums[cur-1] += 1
        return True

    # check rows
    for i in range(0,9):
        if not check_region(i, i, 0, 8, A):
            return False

    #check columns
    for j in range(0,9):
        if not check_region(0, 8, j, j, A):
            return False

    # check grids
    for i in range(0,3):
        for j in range(0,3):
            if not check_region(i*3, i*3+2, j*3, j*3+2, A):
                return False

    return True

A=[
[5, 3, 0, 0, 7, 0, 0, 0, 0],
[6, 0, 0, 1, 9, 5, 0, 0, 0],
[0, 9, 8, 0, 0, 0, 0, 6, 0],
[8, 0, 0, 0, 6, 0, 0, 0, 3],
[4, 0, 0, 8, 0, 3, 0, 0, 1],
[7, 0, 0, 0, 2, 0, 0, 0, 6],
[0, 6, 0, 0, 0, 0, 2, 8, 0],
[0, 0, 0, 4, 1, 9, 0, 0, 5],
[0, 0, 0, 0, 8, 0, 0, 7, 9]]

print(sudoku_checker(A))
