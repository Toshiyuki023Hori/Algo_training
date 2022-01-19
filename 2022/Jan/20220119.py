# https://atcoder.jp/contests/abc200/tasks/abc200_c
import itertools
N = int(input())
a_array = list(map(int, input().split(' ')))
count = 0
# 2 * 10**5C2　ということなので 最大通り数は10**5通り
# 純粋に全探索すれば間に合いそう
for i in itertools.combinations(a_array, 2):
    # ('Ai', 'Aj')の形でループ
    if (int(i[0]) - int(i[1])) % 200 == 0 or (int(i[1]) - int(i[0])) % 200 == 0 :
        count += 1
print(count)
