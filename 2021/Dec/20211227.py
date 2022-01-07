# https://atcoder.jp/contests/abc216/tasks/abc216_b

N = int(input())
name_list = [str(input()) for i in range(N)]
# set前とset後の長さを比べる
origin_len = len(name_list)
name_set = set(name_list)
set_len = len(name_set)
if set_len != origin_len:
    print('Yes')
else :
    print('No')
