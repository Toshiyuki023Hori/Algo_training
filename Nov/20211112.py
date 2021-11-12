# https://atcoder.jp/contests/abc089/tasks/abc089_c
# 別の視点から全検索する

# 10**5C3 の通り数は6,666,599,998通り
# 競プロは2億-10億通りが限界なので、単純な組み合わせの計算では不可能

N = int(input())
# そもそも[M,A,R,C,H]以外から始まる名前はlistに入れなければいい
name_list = []
for i in range(N):
    name = input()
    if name[0] == 'M' or name[0] == 'A' or name[0] == 'R' or name[0] == 'C' or name[0] == 'H':
        name_list.append(name)
# Nよりもlen(name_list)の方が少ないから、range(N)は使えない
count = 0
ans = 0
if len(name_list) > 2:
    for i in range(len(name_list)):
        count += 1
        for j in range(i + 1, len(name_list)):
            if name_list[i][0] != name_list[j][0]:
                count += 1
                for k in range(j + 1, len(name_list)):
                    if name_list[i][0] != name_list[j][0] and name_list[j][0] != name_list[k][0] and name_list[i][0] != name_list[k][0]:
                        count += 1
                        # print(f'{name_list[i]} and {name_list[j]} and {name_list[k]}')
                        # print(count)
                        if count == 3:
                            ans += 1
                            count = 2
            count = 1
        count = 0
    print(ans)
else :
    print(0)
