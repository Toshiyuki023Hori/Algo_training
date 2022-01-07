# https://atcoder.jp/contests/abc120/tasks/abc120_c

num_list = input()
# 0と1の数で判断
# 0: 6個, 1: 8個 => 6個取り出せる
num_of_0 = num_list.count('0')
num_of_1 = num_list.count('1')
# 判定 1 : listの数が1つだけではないか
# 判定 2 : 0か1片方の数字しか入っていないか
if len(num_list) != 1 and num_of_0 != 0 and num_of_1 != 0:
    print(min(num_of_0, num_of_1)*2)
else :
    print(0)