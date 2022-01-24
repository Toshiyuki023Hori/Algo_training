# https://atcoder.jp/contests/arc133/tasks/arc133_a

### 結局解けませんでした
# import itertools
# import copy
# N = input()
# A_ARRAY = list(map(int, input().split()))
# # sorted_a_array = sorted(A_ARRAY)
# a_set = set(A_ARRAY)
# # 各xの調査のためにsetを作成
# unique_a_list = list(a_set)
# ans = []
# # removeは当てはまるものを全てarrayから取り除く
# for i in unique_a_list:
#     # removeは破壊的メソッドなので、処理される用の配列を用意
#     # ただの代入だと shallow copy となって、破壊的メソッドの処理はコピー元にも影響するから、deepcopyを使う
#     a_array_for_delete = copy.deepcopy(A_ARRAY)
#     while i in a_array_for_delete:
#         a_array_for_delete.remove((i))
#     permutated_list = list(itertools.permutations(a_array_for_delete))
#     isFirst = True
#     for combo in permutated_list:
#         if ans == [] and isFirst :
#             ans = permutated_list[0]
#             isFirst = False
#         else :
#             loop_len = min(len(ans), len(permutated_list[0]))
#             for i in range(loop_len):
#                 if not ans[i] >= permutated_list[0][i]:
#                     break
#             ans = permutated_list[0]
# print(ans)


### 以下、ABCの問題
# https://atcoder.jp/contests/abc236/tasks/abc236_c
N, M = map(int, input().split(' '))
S_ARRAY = list(map(str, input().split()))
T_ARRAY = list(map(str, input().split()))
# 考え方としては、急行列車は普通列車に内包されている形をとる
# 普通列車でループを回して、急行列車のn個目の駅か判定していけば良いのでは?
# なので、考えられる計算量はO(N)(Nは普通列車の駅の個数)
t_idx = 0
for s_station in S_ARRAY:
    if s_station == T_ARRAY[t_idx] :
        print('Yes')
        t_idx += 1
    else :
        print('No')
