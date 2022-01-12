# https://atcoder.jp/contests/abc200/tasks/abc200_b
N, K = map(int, input().split(' '))
for i in range(K):
    if N % 200 == 0:
        N = int(N / 200)
    else :
        N = str(N) + '200'
        N = int(N)
print(N)
