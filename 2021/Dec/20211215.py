# https://atcoder.jp/contests/abc215/tasks/abc215_c

import itertools
S, K = input().split(' ')
# sorted()は itrable としてreturn
# ""とjoin()してあげることで、strになる
sorted_S_list = sorted(S)
sorted_S_str = "".join(sorted_S_list)
str_permutations = set(itertools.permutations(sorted_S_str, len(sorted_S_str)))
str_permutations_list = list(str_permutations)
# indexが0から始まるのでn番目-1
print("".join(str_permutations_list[int(K)-1]))
