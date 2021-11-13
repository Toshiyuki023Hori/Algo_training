# https://atcoder.jp/contests/abc089/tasks/abc089_c
# 別の視点から全検索する

# 10**5C3 の通り数は6,666,599,998通り
# 競プロは2億-10億通りが限界なので、単純な組み合わせの計算では不可能

# これはわしの間違った回答  ============================

            # N = int(input())
            # # そもそも[M,A,R,C,H]以外から始まる名前はlistに入れなければいい
            # name_list = []
            # for i in range(N):
            #     name = input()
            #     if name[0] == 'M' or name[0] == 'A' or name[0] == 'R' or name[0] == 'C' or name[0] == 'H':
            #         name_list.append(name)
            # # Nよりもlen(name_list)の方が少ないから、range(N)は使えない
            # count = 0
            # ans = 0
            # if len(name_list) > 2:
            #     for i in range(len(name_list)):
            #         count += 1
            #         for j in range(i + 1, len(name_list)):
            #             if name_list[i][0] != name_list[j][0]:
            #                 count += 1
            #                 for k in range(j + 1, len(name_list)):
            #                     if name_list[i][0] != name_list[j][0] and name_list[j][0] != name_list[k][0] and name_list[i][0] != name_list[k][0]:
            #                         count += 1
            #                         # print(f'{name_list[i]} and {name_list[j]} and {name_list[k]}')
            #                         # print(count)
            #                         if count == 3:
            #                             ans += 1
            #                             count = 2
            #             count = 1
            #         count = 0
            #     print(ans)
            # else :
            #     print(0)

### =====================================

# 正しい回答
# 考え方: 各名前の先頭の文字が何個あるか調べる(名前は全てuniqueだから)

from collections import defaultdict
import itertools

N = int(input())
# defaultdictを使う理由
# -> 標準のdictは存在しないkeyに処理をしようとするとerrorになる
# -> 今回は頭文字のアルファベットの数を数えるもの、初めて出てくるアルファベットならifで存在チェックしないといけない
# -> defaultdictなら存在チェック不要
D = defaultdict(int)

for _ in range(N):
    S = input()
    # dict型に、{"alphabet" : "the number of key alphabet"}で保存
    D[S[0]] += 1
ans = 0
A = ['M', 'A', 'R', 'C', 'H']
for c in itertools.combinations(A, 3):
    # ループは以下のように回る
    # ('M', 'A', 'R')
    # ('M', 'A', 'C')
    # ...
    # 要は、startwith('M'): 2, startwith('A'): 1, startwith('R'): 3
    # なら、それぞれの名前がその数あるということで、
    # その3種で構成される名前の組み合わせの数を把握しないといけない
    # 5C3の組み合わせを列挙 => 各組み合わせが何通りあり得るかを取得 => ansに足していく
    ans += D[c[0]]*D[c[1]]*D[c[2]]
print(ans)
