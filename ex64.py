def replace_and_remove(s, size):
    count_a = 0;
    current_pos = 0;
    write_pos = 0;

    # forward pass
    for _ in range(size):
        c = s[current_pos];
        if c == 'a':
            count_a += 1;
            s[write_pos] = s[current_pos];
            write_pos += 1;
            current_pos += 1;
        elif c == 'b':
            current_pos += 1;
        else: # c!=b and c!=a
            s[write_pos] = s[current_pos];
            write_pos += 1;
            current_pos += 1;

    current_pos = write_pos - 1;
    write_pos = write_pos + count_a - 1;

    #backward pass
    while current_pos >= 0:
        c = s[current_pos];
        if c == 'a':
            s[write_pos] = 'd';
            s[write_pos-1] = 'd';
            write_pos -= 2;
            current_pos -= 1;
        else:
            s[write_pos] = s[current_pos];
            write_pos -= 1;
            current_pos -= 1;

mystring = ['a', 'c', 'd', 'b', 'b', 'c', 'a', 'h', 'e', 'l', 'l', 'o'];
replace_and_remove(mystring, len(mystring));
print(mystring);
