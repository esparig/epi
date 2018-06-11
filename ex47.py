def power(x, y):
    result = 1
    while y:
        p = y & ~(y-1)
        print (p)
        y -= p
        result *= x<<(p-1)
    return result

print(power(5, 29))
print(power(3, 3))
print(power(2, 7))
