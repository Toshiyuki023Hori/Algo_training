# https://atcoder.jp/contests/abc128/tasks/abc128_c

# bit全探索の練習問題

# 入力の意味
# 2行目-最終行-1 の左列は、何個電球があるかを表したもの

# 5 2
# 3 1 2 5
# 2 2 3
# 1 0


N, M = map(int, input().split())
lamp_dat = [list(map(int, input().split()))[1:] for _ in range(M)]

# スイッチを中心に考えることにしたので、ランプ毎に
# 与えられている情報を、スイッチ毎にどのランプに
# 繋がっているかに変換している。
# ついでに 1-indexed を 0-indexed にしておく。
switches = [[] for _ in range(N)]
for i, sw_list in enumerate(lamp_dat):
    # 最初の数字は個数なので抜いておくこと
    for sw in sw_list[1:]:
        switches[sw-1].append(i)

# 結局ランプにつながったスイッチが押されるたび、
# ランプは ON/OFF を繰り返す。

# そこで、ライトが全て点灯する条件を、二進法で数値に変換して持っておく
# ことで、あとで条件を比較するのが楽になる。
# ビット探索の関係上、順番が逆になる（ランプ 1 が下の桁になる）
# ので [::-1] と逆順にしてある。
lit_cond = int(''.join(input()[::-1].split()), 2)

# ビット全探索
# スイッチON: 1
# スイッチOFF: 0
# として、二進法で 0000... ～ 1111... まで探索を行う
result = 0
for st in range(1<<N):
    # もちろん、ランプ毎にいくつスイッチが押されているかを確認し、
    # 2 で割って点灯しているかどうか確認するという素直な
    # 実装もあるが、ここでは少し違ったやり方で解いている。

    # 各ランプのステータスをビットで管理していく
    lamp_status = 0

    # スイッチ毎に ON になっているかどうかを確認し、
    # ON なら lamp_status を変化させる
    for i in range(N):
        # スイッチは ON ？
        if st>>i & 1:
            for lmp in switches[i]:
                # あるランプにつながっているスイッチが押されるたびに、
                # 該当する lamp_status のビットを xor で反転させている。
                lamp_status = lamp_status ^ (1<<lmp)
    # 全部点灯してるなら、答えに +1
    if lamp_status == lit_cond:
        result += 1

print(result)
