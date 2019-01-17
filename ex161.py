from collections import defaultdict

def count_score_combinations(final_score):
    d = defaultdict(set)
    d[0].add((0,0,0))
    d[2].add((1,0,0))
    d[3].add((0,1,0))
    d[4].add((2,0,0))
    d[5].add((1,1,0))
    d[6].add((3,0,0))
    d[6].add((0,2,0))
    d[7].add((2,1,0))
    d[7].add((0,0,1))

    def score_comb(s):

        if s in d.keys():
            return d[s]

        if s-2 >= 2:
            set_s = score_comb(s-2)
            for comb in set_s:
                d[s].add((comb[0]+1, comb[1], comb[2]))
        if s-3 >= 2:
            set_s = score_comb(s-3)
            for comb in set_s:
                d[s].add((comb[0], comb[1]+1, comb[2]))

        if s-7 >= 2:
            set_s = score_comb(s-7)
            for comb in set_s:
                d[s].add((comb[0], comb[1], comb[2]+1))
        if s in d:
            return d[s]
        return set()

    result = score_comb(final_score)
    print(result)
    return len(result)

print("Possible combinations:", count_score_combinations(42))
