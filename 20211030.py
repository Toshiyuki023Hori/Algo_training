# https://atcoder.jp/contests/abc225/tasks/abc225_a

from itertools import permutations
s = input()
print(len(set(permutations(s))))

# https://atcoder.jp/contests/abc225/tasks/abc225_b

n = input()
star_list = [input().split()  for _ in range(int(n)-1)]
print(star_list)
# 必ず a < b
# bに続く頂点は + 1のみ

