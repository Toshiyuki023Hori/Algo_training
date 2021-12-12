# https://atcoder.jp/contests/abc215/tasks/abc215_b

# N < 10**18
# *2 したところで桁数が上がるわけではない
# しかし、10 ** 18 < 2 ** i を試行したところ i = 60 だったので、
# 10 ** 5 以内の計算量の制約は十分満たす
N = int(input())
i = 0
while 2 ** i < N:
    i += 1
print(i)
