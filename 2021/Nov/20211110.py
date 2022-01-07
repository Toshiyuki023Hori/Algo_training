# https://atcoder.jp/contests/s8pc-6/tasks/s8pc_6_b
# 通り数を見積もる全探索
# 1. 入り口と出口を決定する[これはsortしてそれの中央値になる]
# 2. それに向かう分を全探索

N = int(input())
item_places_array = []
enter_array = []
exit_array = []

for i in range(N):
    one_raw = list(map(int, input().split()))
    enter_array.append(one_raw[0])
    exit_array.append(one_raw[1])
    item_places_array.append(one_raw)
enter_array.sort()
exit_array.sort()
print(enter_array)
print(exit_array)
# 大きさが真ん中のものが入り口と出口に決定される
enter_num = enter_array[N//2]
exit_num = exit_array[N//2]

# 各列で差を求めてやればいい
# 段階としては3段階
# ENTER-A | A-B | B-EXIT
# 以上3段階の和
total_seconds = 0
for item_place in item_places_array:
    total_seconds += abs(enter_num - item_place[0]) + abs(item_place[0] - item_place[1]) + abs(item_place[1] - exit_num)
print(total_seconds)
