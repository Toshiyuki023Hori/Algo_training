# https://atcoder.jp/contests/abc106/tasks/abc106_b

# 約数の個数はN/2までで全てわかる

n = int(input())
count = 0
ans = 0
for i in range(1, n + 1):
    if i % 2 == 1:
        for j in range(1, round(i/2) + 1):
            if i % j == 0:
                count += 1
        # i/2の分で計算すると、i/1で割った時にi自身の数が約数でカウントされないので、
        # 約数の個数の確認: count は 7 で条件分岐
        if count == 7:
            ans += 1
    count = 0
print(ans)

