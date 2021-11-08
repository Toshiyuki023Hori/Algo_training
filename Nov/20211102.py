# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_B&lang=ja

# 問題文に直接「11 以上 NN 以下について調べてください」といったようなことが書かれていなくても、
# あり得る状態が何通りあるか考えるのは重要です。

# このような (i,j,k)(i,j,k) の組は高々 100×99×986=161700100×99×986=161700 通りとなり、
# 全通り試しても十分間に合います。これが全探索の 2 つ目の考え方です。
# 競プロは2億 ～ 10億通り程度しか探索できない

n, x = map(int, input().split())
count = 0
for i in range(n + 1):
    for j in range(i + 1, n + 1):
        for k in range(j + 1, n + 1):
            if i + j + k == x:
                count += 1
print(count)

# ===========================================

# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_b

# 小数点以下切り捨て
# 複数考えられる => n/1.08の切り捨てで出た答えを保存
# 保存した数字の+=1 分の数字を *1.08 して n になるかチェック

import math
n = int(input())
floor_n = math.floor(n / 1.08)
ceil_n = math.ceil(n / 1.08)
is_success = False
for i in range(floor_n - 1, floor_n + 1):
    if math.floor(i * 1.08) == n:
        print(i)
        is_success = True
        break
if not is_success:
    for i in range(ceil_n - 1, ceil_n + 1):
        if math.floor(i * 1.08) == n:
            print(i)
            is_success = True
            break
if not is_success:
    print(':(')
