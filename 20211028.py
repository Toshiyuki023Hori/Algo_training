# https://atcoder.jp/contests/abc214/tasks/abc214_b

s, t = map(int, input().split())
ans = 0
for i in range(s+1):
    for j in range(s-i+1):
        for k in range(s-i-j+1):
            if i * j * k <= t:
                ans += 1

print(ans)

