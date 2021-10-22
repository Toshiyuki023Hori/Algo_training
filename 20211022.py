# https://atcoder.jp/contests/abc212/tasks/abc212_c

# 入力例
# 6 8
# 82 76 82 82 71 70
# 17 39 67 2 45 35 22 24

# 考え方
# 一方の最大値 ー もう片方の最小値を計算して小さい方を出せばいい

# 正解(考え方)
# 二分探索
# あえてライブラリを使わない方法で

# split() => 引数なしは空白ごと
n, m = map(int, input().split())
# len_num_list => ['a', 'b']
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
a_list.sort()
b_list.sort()
ans = 99999

# aの各数に近いものをbを二分探索して探す
for a_num in a_list:
    for i in range(len(b_list)):
        left_i = 0
        right_i = len(b_list) - 1
        
        while left_i <= right_i:
            middle_i = (left_i + right_i) // 2
            middle_val = b_list[middle_i]
            # 探している数が、中央値?よりも小さい場合、
            # 左半分にあるということだから、中央値のインデックスを、
            # right_iに変更して、左半分の中でまた二分探索をする
            if a_num < middle_val:
                right_i = middle_i - 1
                continue
            if a_num > middle_val:
                left_i = middle_i + 1
                continue
        if ans >= abs(a_num - b_list[(left_i + right_i) // 2]):
            ans = abs(a_num - b_list[(left_i + right_i) // 2])
        print(ans)
print(ans)


# Runtime Overしたので
# ライブラリ使う

import bisect

n, m = map(int, input().split())
# len_num_list => ['a', 'b']
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
a_list.sort()
b_list.sort()
ans = int(1e9)

for i in range(n):
    point = bisect.bisect_left(b_list, a_list[i])
    # bisect_left は 挿入可能なindexを返す
    if point != 0:
        tmp = abs(a_list[i] - b_list[point - 1])
    else:
        tmp = abs(a_list[i] - b_list[point])
    if point != len(b_list):
        tmp2 = abs(a_list[i] - b_list[point])
    else:
        tmp2 = abs(a_list[i] - b_list[point-1])
    ans = min(ans, tmp)
    ans = min(ans, tmp2)
    
print(ans)

