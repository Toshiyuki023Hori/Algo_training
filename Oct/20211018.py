# https://atcoder.jp/contests/abc219/tasks/abc219_b
s_list = [input()  for i in range(3)]
t = input()
ans = ''
# tはlistのインデックスよりプラスした数なので、
# ループ処理で ti - 1 したインデックスで s_list の値を呼び出す
# list に入れることで条件分岐をしなくて済む
for index in t:
    ans += s_list[int(index) - 1]
print(ans)