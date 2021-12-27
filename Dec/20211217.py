# https://atcoder.jp/contests/abc216/tasks/abc216_c
# 魔法B(n * 2)を119回すると、664,613,997,892,457,936,451,903,530,140,172,288
# 制約のN < 10**18 よりも遥かに多い
# したがって、n * 2 が N を超えない限りはBを使って、それ以外はAを使うと最短

# これだとTLEになった
            # N = int(input())
            # # 開始が0なので、Aを一回実行して1にする
            # # A実行済なのでansは'A'からスタート
            # ball_count = 1
            # ans = 'A'
            # # このループで限りなくBを実行
            # while ball_count * 2 <= N:
            #     ball_count *= 2
            #     ans += 'B'
            # # このループで N になるまでAを実行
            # while ball_count + 1 <= N or len(ans) > 120:
            #     ball_count += 1
            #     ans += 'A'
            # print(ans)


# 考え方を変えて、
# Nから 奇数なら"-1"偶数なら"/2"を繰り返す
N = int(input())
calc_doc_str = ''
while N > 0:
    if N % 2 == 0:
        N = N // 2
        calc_doc_str = 'B' + calc_doc_str
    else:
        N -= 1
        calc_doc_str = 'A' + calc_doc_str
print(calc_doc_str)

# Python3で割り算に/を使うと、結果はfloatになります。
# そして、floatの有効桁は16桁弱です。
# しかし、この問題の入力の最大は10^18なので、floatで表現できる範囲を超えています。

# 実際、以下のような入力に対して、(2^54+2) = 18014398509481986
# 正しい結果は以下ですが、

# ABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBAB

# ご呈示のコードですと以下になります。(末尾近くのAが無い)

# ABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB

