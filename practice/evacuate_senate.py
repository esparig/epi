def evacuate_senate(p):
    c = 'A'
    n = []
    for i in range(len(p)):
        n.append(c)
        c = chr(ord(c)+1)
    P = [(p[i], i) for i in range(len(p))]
    P.sort()
    sorted_p , perm = zip(*P)
    print(sorted_p , perm)

evacuate_senate([5, 7, 2, 2])
