def int2str(num):
    isneg = False;
    s = [];
    if num < 0:
        isneg = True;
        num = -num;
    while num > 0:
        cur = num % 10;
        num = num // 10;
        s.append (chr(ord('0') + cur));
    if isneg:
        return "-"+"".join(reversed(s));
    return "".join(reversed(s));

def str2int(str):
    isneg = False;
    num = 0;
    for s in str:
        num *= 10;
        if s == '-':
            isneg = True;
        else:
            num += ord(s) - ord('0');
    if isneg:
        return -num;
    return num;

print(int2str(-123));
print(int2str(-2));
print(str2int("-123"));
print(str2int("-2"));
