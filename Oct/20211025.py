# https://atcoder.jp/contests/abc213/tasks/abc213_c

# 多分ループ回してたら追いつかない
# ある文字を複製するような関数

# AtCoder Beginner Contest 213
# C - Reorder Cards

import bisect

h, w, n = map(int,input().split())

A = []
B = []
for i in range(n):
    a, b = map(int,input().split())
    A.append(a)
    B.append(b)

print(A)
print(B)

X = list(set(A))
# setでは元の順序が無視されるためsort()
X.sort()
print(f'X is {X}')
Y = list(set(B))
Y.sort()
print(f'Y is {Y}')

for i in range(n):
    C = bisect.bisect_left(X, A[i]) + 1
    print(f'C is {C}')
    D = bisect.bisect_left(Y, B[i]) + 1
    print(f'D is {D}')
    print(str(C) + " " + str(D))