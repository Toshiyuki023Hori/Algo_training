# https://atcoder.jp/contests/abc214/tasks/abc214_b


S, T = map(int, input().split(' '))

# https://math.nakaken88.com/textbook/expert-combination-of-integers-whose-sum-is-the-given-value/
# この記事より目標となる合計値から2つ取った組み合わせを求めればいいことがわかる

# ans = 0
# for i in range(S+1):
#     for j in range(S+1):
#         for k in range(S+1):
#             if i + j + k <= S and i * j * k <= T:
#                 ans += 1
# print(ans)


# 下記のように、-i, -i-j とした方が通り数を減らせる
ans = 0
for i in range(S+1):
    for j in range(S-i+1):
        for k in range(S-i-j+1):
            if i + j + k <= S and i * j * k <= T:
                ans += 1
print(ans)
