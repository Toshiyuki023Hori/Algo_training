#-*- coding: utf-8 -*-

# https://atcoder.jp/contests/abc150/tasks/abc150_c

# 辞書順とは、ご想像の通り複数の文字列を比べたときに、同番目であるにも関わらず、
# a, o などと文字が違った場合、アルファベット順で「早い」方を「小さい」とする順番
    
# split('any_char') は指定した文字で区切った "list" で返ってくる
import itertools
n = input()
p_tuple = tuple(map(int, input().split()))
q_tuple = tuple(map(int, input().split()))
# 指定した範囲の順列を出す
# rangeは0からスタートするから、最大数が -1 される点に注意
# 例: range(3) => 0, 1, 2
permutations = itertools.permutations(range(1, int(n) + 1))
# permutations_list: [(1, 2, 3), (3, 2, 1) ...]
# tupleで格納される
a = ''
b = ''
# enumerate関数は、listやtupleの値とインデックスを同時に取得
# 例: (2, 4, 6) => printすると, 0 / 2 , 1 / 4, 2 / 6 で返ってくる
for index, value in enumerate(permutations):
    if value == p_tuple:
        a = index
    if value == q_tuple:
        b = index
# abs()で絶対値を算出
print(abs(a-b))
