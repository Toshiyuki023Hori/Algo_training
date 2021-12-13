# https://atcoder.jp/contests/abc145/tasks/abc145_c
# 想定される最大の通り数は8!通り = 40,320通り < Atcoderの最大の見積もり100,000よりも少ない
# けど,itertool.permutationと、forループで2回ほど繰り返すからギリギリ足りるか、制限超えるか

import itertools, math
N = int(input())
all_town_array = [input().split(' ') for i in range(N)]
using_itertool_array = [i for i in range(N)]
all_combinations = list(itertools.permutations(using_itertool_array, N))
sum = 0
# all_town_array = [['0', '0'], ['1', '0'], ['0', '1']] == [[xi, yi], [xj, yj], [xk, yk]]
# all_combinations[(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0)...]
for one_set in all_combinations:
    # 最後のindex-1で計算完了できる
    # one_set = (0, 1, 2)
    for i in range(len(one_set)-1):
        # 平方根 => X ** 0.5 = √X
        x = (int(all_town_array[one_set[i]][0]) - int(all_town_array[one_set[i+1]][0])) ** 2
        y = (int(all_town_array[one_set[i]][1]) - int(all_town_array[one_set[i+1]][1])) ** 2
        distance = x+y
        distance = math.sqrt(distance)
        sum += distance
print(sum/len(all_combinations))

# 提出結果: 一発クリア(https://atcoder.jp/contests/abc145/submissions/27899674)
# 予測通り制限時間120sギリギリ
