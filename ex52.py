def increment_integer(D):
    size = len(D)
    carry = 1

    for i in range(size-1, -1, -1):
        result = D[i] + carry
        if result > 9:
            carry = 1
            D[i] = result % 10
        else:
            carry = 0
            D[i] = result
    if carry > 0:
        return [carry]+D
    return D

print([1, 2, 3], "->", increment_integer([1, 2, 3]))
print([1, 9, 9], "->", increment_integer([1, 9, 9]))
print([9, 9, 9], "->", increment_integer([9, 9, 9]))
