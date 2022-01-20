# https://atcoder.jp/contests/abc200/tasks/abc200_c
#### import itertools
#### N = int(input())
#### a_array = list(map(int, input().split(' ')))
#### count = 0
#### # 2 * 10**5C2　ということなので 最大通り数は10**5通り
#### # 純粋に全探索すれば間に合いそう
#### for i in itertools.combinations(a_array, 2):
####     # ('Ai', 'Aj')の形でループ
####     if (int(i[0]) - int(i[1])) % 200 == 0 or (int(i[1]) - int(i[0])) % 200 == 0 :
####         count += 1
#### print(count)


# --- 以下に正解を書く
# Ai−Aj が 200 の倍数とはつまり、Ai と Aj を 200 で割った余りが等しいということです
# 愚直な二重ループで書くと、以下のようなことをしたいです。このコードは O(N2) ですから、N≤200,000 の制約ではTLEになります。
# そこで、0 ～ 199 の 200 種類の値が、今までに何回出てきたかカウントするリスト cnt を作ります。

N = int(input())
A = list(map(int, input().split()))

R = [x % 200 for x in A]
# 要素が反復したリストを作っている
# 下なら [0, 0, 0, 0, ...](200個ある)
cnt = [0] * 200

ans = 0
for r in R:  # range(j)と書いてもいいですが、これでも左から順に見てくれます
    print(r)
    print(cnt[r])
    ans += cnt[r]
    cnt[r] += 1
print(ans)
