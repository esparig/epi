def reverse_words(s):
    s.reverse()
    i = 0
    blank = s.find(b" ")

    while True:
        aux = s[i:blank]
        aux.reverse()
        s[i:blank] = aux
        i = blank + 1
        cur = s[i:].find(b" ")
        if cur == -1:
            break
        blank += cur + 1
    aux = s[i:]
    aux.reverse()
    s[i:] = aux
    return s

frase = "Alice will like Bob"
print(frase, "->", reverse_words(bytearray(frase, 'utf8')).decode('utf8'))
