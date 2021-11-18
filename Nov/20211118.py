# https://atcoder.jp/contests/abc120/tasks/abc120_b

import math
# 最大公約数の約数を列挙する
A, B, K = map(int, input().split())
greatest_common_divisor = math.gcd(A, B)
divisors_list = []
for i in range(1, greatest_common_divisor + 1):
    if greatest_common_divisor % i == 0:
        divisors_list.append(i)
divisors_list.sort()
# K番目に大きい = sort()は昇順だから、"-"スタートにすれば実装は簡単
print(divisors_list[-K])


