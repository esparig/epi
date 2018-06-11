def get_profit(S):
    t = len(S);
    i, j = t - 2, t - 1;
    current_max_profit = 0;
    while i >= 0:
        if S[i] > S[j]:
            j = i;
            i -= 1;
        profit = S[j] - S[i];
        if profit > current_max_profit:
            current_max_profit = profit;
        i -= 1;
    return current_max_profit;

Stock = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250];
print(get_profit(Stock));
