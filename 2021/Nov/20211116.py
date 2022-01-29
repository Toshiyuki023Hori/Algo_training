# bit 全探索編
# 『bit全探索』という名前が難しそうで、イメージがつきづらいのがとっつきづらい原因だと思っています。実際にやっていることは『使う・使わないを全探索』『選ぶ・選ばないを全探索』程度のことです。これなら簡単そうに見えませんか。

# https://atcoder.jp/contests/abc136/tasks/abc136_b

## 解法(ループ使わずにパフォーマンス重視) ==================

# 条件分岐が複雑になって、コードとしての可読性が落ちるため断念

# N = int(input())
# # count = 0
# # 要は、1~9, 100~999(10^2), 10000~99999(10^4)
# # for i in range(1, N + 1):
# if N <= 9:
#     print(N)
# if 100 <= N and N <= 999:
#     print(9 + N - 100 + 1)
# if 10000 <= N and N <= 99999:
#     print(9 + N - 100 + 1 + N - 10000 + 1)

# ==================================

## 解法(全探索loop ver) =========================

N = int(input())
count = 0
# 要は、1~9, 100~999(10^2), 10000~99999(10^4)
for i in range(1, N + 1):
    if i <= 9 or 100 <= i and i <= 999 or 10000 <= i and i <= 99999:
        count += 1
print(count)

## =============================================