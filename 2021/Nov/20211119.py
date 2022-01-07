# https://atcoder.jp/contests/abc057/tasks/abc057_c
N = int(input())

# √N が約数としては最大
# √N 以下は全てペアで見つかるから、調べる数は√Nまででいい
# 約数については10/14のalgoを参照
ans = 100
for i in range (1, round(N ** 0.5) + 1):
    if N % i == 0:
        # 最小を求めればいいから、a/bのペアは作らない
        a = i
        b = N // i
        f = max(len(str(a)), len(str(b)))
        if f < ans:
            ans = f
print(ans)


