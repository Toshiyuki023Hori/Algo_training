#-*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc150/tasks/abc150_b

# n = input()
# a = input()

n = '33'
a = 'ABCCABCBABCCABACBCBBABCBCBCBCABCB'

count = 0
# 3文字連続だから残り2文字で判定はいらない
for i in range(int(n) - 2):
    print(a[i])
    # 頭文字Aのみ処理走らせる
    if a[i] == 'A':
        # 3文字が全部合ってるか判定
        if a[i + 1] == 'B' and a[i + 2] == 'C':
            count += 1
        else :
            continue
    else :
        continue
print(count)
