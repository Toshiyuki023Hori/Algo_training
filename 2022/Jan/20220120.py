# https://atcoder.jp/contests/abc201/tasks/abc201_c
S = input()
ok_num = []
ng_num = []

count = 0

for i, s in enumerate(S):
    if s == 'o':
        ok_num.append(str(i))
    if s == 'x':
        ng_num.append(str(i))


def is_num_ok(num: str) -> bool:
    for o in ok_num:
        if o == '0' and len(num) <= 3:
            continue
        if not(o in num):
            return False
    for n in ng_num:
        if n == '0' and len(num) <= 3:
            return False
        if n in num:
            return False
    return True


for j in range(10000):
    str_j = str(j)
    if is_num_ok(str_j):
        count += 1

print(count)
