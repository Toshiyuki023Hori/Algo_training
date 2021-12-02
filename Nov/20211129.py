# coding: UTF-8
# Syntax Error回避用

# https://qiita.com/gogotealove/items/11f9e83218926211083a
# bit全探索練習問題

# bit全探索で大事な考えは、通り数を2進数で保存すること
# 買う場合は 1 、買わない場合は 2


money = 300
item = (('みかん', 100), ('りんご', 200), ('ぶどう', 300))
n = len(item)
for i in range(2 ** n):
    bag = []
    total = 0

# bit演算の論理積の仕組み

# num = 3
# shift_num = 2
# print(bin(num))
# print(bin(num >> shift_num))
# print(num >> shift_num)

# みたいに具体例があるとわかりやすい
# とにかく全ての基準は2進数である
# 例えば、3 >> 1の答えは、1となる。
# これは3が2進数で表すと、0b11であって、2進数部分を1だけ右シフトすると、
# 0b1という数字が得られる。
# これを10進数で表すと1となるため、 3 >> 1 の答えは 1となる

    for j in range(n):  # このループが一番のポイント
        print(f'i is {i}({bin(i)}) and j is {j}')
        print(f'左シフトは{(i >> j)} & {0b1 >> j} の論理積は {(i >> j) & 1}')
        # 2 進数表記した場合の下から数えて n 桁目（一番下の桁を 0 とします）が 1 であるかどうかをチェックするためのコード
        
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            bag.append(item[j][0])  # フラグが立っていたら bag に果物を詰める
            total += item[j][1]  # 買い物累計額にも加算
    if (total <= money):
        print(total, bag)
    print('==========')


