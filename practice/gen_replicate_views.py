def gen_replicate_views(type_views):
    #ex: type_views = [C, N, C, N, N, C, C]
    #lastC, lastN = -1, -1
    lastC, lastN = next((i for i, v in enumerate(type_views) if v == "C"), -1), next((i for i, v in enumerate(type_views) if v == "N"), -1)
    if lastC == -1 or lastN == -1:
        return None
    result = []
    v = 0
    for i in range(12):
        if i & 1 == 0: #even -> expect Color
            if len(type_views) > v and type_views[v] == "C":
                result.append(v)
                lastC = v
                v += 1
            else:
                result.append(lastC)
        else: #odd -> expect NIR
            if len(type_views) > v and type_views[v] == "N":
                result.append(v)
                lastN = v
                v += 1
            else:
                result.append(lastN)
    print(result)

gen_replicate_views(["C", "N", "C", "N", "N", "C", "C"])
gen_replicate_views(["N", "C", "N", "N", "C", "N", "N"])
gen_replicate_views(["N", "N", "N", "N", "N"])
