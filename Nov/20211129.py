# https://qiita.com/gogotealove/items/11f9e83218926211083a
# bit全探索練習問題

# bit全探索で大事な考えは、通り数を2進数で保存すること
# 買う場合は 1 、買わない場合は 2
wallet = 300
items = (("みかん", 100), ("りんご", 200), ("ぶどう", 300))
n = len(items)
# なぜ 2**n となるか

for i in range(2 ** n):
    bag = []
    print("pattern {}: ".format(i), end="")
    for j in range(n):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            bag.append(item[j][0])  # フラグが立っていたら bag に果物を詰める
    print(bag)
        

