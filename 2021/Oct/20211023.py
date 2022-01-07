# https://atcoder.jp/contests/abc224/tasks/abc224_a
s = input()
if s[len(s) - 2] == 'e' and s[len(s) - 1] == 'r':
    print('er')
elif len(s) >= 3 and s[len(s) - 3] == 'i' and s[len(s) - 2] == 's' and s[len(s) - 1] == 't':
    print('ist')

# https://atcoder.jp/contests/abc213/tasks/abc213_b

# 考え方
# sortして上から二つ目をprint

n = input()
a_list = list(map(int, input().split()))
# list.sort() は元のlistを並び替え
# sorted() は 新しいlistを作成
sorted_a_list = sorted(a_list)
print(a_list.index(sorted_a_list[-2]) + 1)