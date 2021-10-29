# https://atcoder.jp/contests/abc215/tasks/abc215_b
n = int(input())
ans = 0
for num in range(n//2):
    if 2 ** num >= n:
        ans = num
        print(ans)
        break
print(ans)

