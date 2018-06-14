def base_conversion(num_str, b1, b2):
    def base_conv_from_decimal(num, b2, isneg):
        result = [];
        while num > 0:
            cur = num % b2;
            result.append(symbols[cur]);
            num = num // b2;

        if isneg:
            result.append('-');

        return "".join(reversed(result));

    def base_conv_to_decimal(num, b1):
        i = 0;
        result = 0;
        while num > 0:
            cur = num % b1;
            result += cur * pow(b1, i);
            i += 1;
            num = num // b1;
        return result;


    num = int(num_str);
    isneg = False;
    symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'];
    if num < 0:
        isneg = True;
        num = -num;

    print("BASE 10: ", base_conv_to_decimal(num, b1))
    if b1 != 10:
        return base_conv_from_decimal(base_conv_to_decimal(num, b1), b2, isneg);
    else:
        return base_conv_from_decimal(num, b2, isneg);


print(base_conversion('10', 10, 2));
print(base_conversion('10', 10, 16));

print(base_conversion('306', 10, 13));
print(base_conversion('1010', 2, 16));
print(base_conversion('615', 7, 13));
