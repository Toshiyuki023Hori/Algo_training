# https://atcoder.jp/contests/abc223/tasks/abc223_b

from itertools import permutations
s = input()
# permutations => [('b', 'o', 'y'), ('y', 'o', 'b'), ...]という風に一文字ずつに分けられる
# join()で整形
# '[any_char]'.join(list) => 'list[i][any_char]list[i+1][any_char]'という風にリスト内のelementを
# 指定した文字挿入して連結する
s_permutated = [''.join(p) for p in permutations(s)]
# setオブジェクト内では、同じ要素は存在できない
s_set = set(s_permutated)
s_list = list(s_set)
s_list.sort()
print(s_list[0])
print(s_list[-1])

# 以下、解説
# 右シフトを 1 回行うことは、左シフト を N−1 回行うことと同じです。そのため、左シフトのみを行うとしてよいです。
# さらに、左シフトを N 回行うと元の文字列に戻るため、左シフトを行う回数は 0 回以上 N−1 回以下であるとしてよいです。
s = input()

result = []
for i in range(len(s)):
    # str[:i] => iまで取得
    # str[i:] => iから取得
    # Pythonのスライスは元の文字列を変更しない
    pulled_str = s[:i]
    left_str = s[i:]
    connected_str = left_str + pulled_str
    result.append(connected_str)
result.sort()
print(result[0])
print(result[-1])
