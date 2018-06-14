def base_conversion(num_str, b1, b2):
    symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'];

    def base_conv_from_decimal(num, b2):
        result = [];

        isneg = False;
        if num < 0:
            isneg = True;
            num = -num;

        while num > 0:
            cur = num % b2;
            result.append(symbols[cur]);
            num = num // b2;

        if isneg:
            result.append('-');

        return "".join(reversed(result));

    def base_conv_to_decimal(num_str, b1):
        isneg = False;
        digits = len(num_str);
        result = 0;
        for s in num_str:
            digits -= 1;
            if s == "-":
                isneg = True;
            else:
                result += symbols.index(s) * pow(b1, digits);
        if isneg:
            return -result;
        return result;

    if b1 != 10:
        decimal = base_conv_to_decimal(num_str, b1);
        if b2 != 10:
            return base_conv_from_decimal(decimal, b2);
        else:
            return decimal;
    else:
        return base_conv_from_decimal(int(num_str), b2);


print(base_conversion('10', 10, 2)); # 1010
print(base_conversion('10', 2, 10)); # 2
print(base_conversion('1010', 2, 16)); # A
print(base_conversion('615', 7, 13)); # 1A7
print(base_conversion('A', 16, 10)); # 10
