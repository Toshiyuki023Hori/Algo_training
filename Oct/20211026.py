# https://atcoder.jp/contests/abc036/tasks/abc036_c

# 座標圧縮
    # 数列 A0,A1,…,AN−1 が与えられたときに、それぞれの要素が「全体の中で何番目に小さいか」を求めていく作業
# 要は大小関係だけを抽出したい
# 参考: https://algo-logic.info/coordinate-compress/


N = int(input())
a_list = [int(input()) for _ in range(N)]

# 重複を除いて大小関係を明確に
a_set = sorted(set(a_list))

# {元の値: 圧縮後の値} で辞書を作成
comp_dic = {val:i for i, val in enumerate(a_set)}

# 変換しつつ出力
for p in a_list:
    print(comp_dic[p])

# 参考
# 入力
        # 5
        # 3
        # 3
        # 1
        # 6
        # 1

# 出力結果
# {1: 0, 3: 1, 6: 2} : comp_dicの中身
# 1
# 1
# 0
# 2
# 0
