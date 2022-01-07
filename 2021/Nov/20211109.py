# https://atcoder.jp/contests/abc122/tasks/abc122_b
# 線形探索(全探索)の問題

S = input()
count = 0
for i in range(len(S)):
    j = i
    temp = 0
    while S[j] == 'A' or S[j] == 'C' or S[j] == 'G' or S[j] == 'T':
        temp += 1
        j += 1
        if j == len(S):
            break
    if count < temp:
        count = temp
print(count)

