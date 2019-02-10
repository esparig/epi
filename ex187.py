import collections

def shortest_sequence(s, t):
    def differ_one_char(a, b):
        one_found = False
        for i in range(len(a)):
            if a[i] != b[i]:
                if one_found:
                    return False
        return one_found

    if s==t:
        return 0
    q = collections.deque()
    q.append((s, 0))
    while q:
        cur = q.popleft()
        for w in D[cur[0]]:
            if w==t:
                return cur[1]+1
            q.append((w, cur[1]+1))
    return -1

def connect(a, b):
    D[a].append(b)
    D[b].append(a)

D = collections.defaultdict(list)

connect("bat", "cat")
connect("cat", "cot")
connect("cot", "dot")
connect("dot", "dog")

print(shortest_sequence("dog", "dog"))
