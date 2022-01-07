# https://atcoder.jp/contests/abc227/tasks/abc227_c
# Pythonとpypyで処理の速度が違う模様
# https://qiita.com/OKCH3COOH/items/f0c5c4681bc30dddf7f4

# 入力の受け取り
N=int(input())

# 答えのカウント
ans=0

# A=1~(10^6-1)まで
# 
for A in range(1,10**6):
    # N<A^3なら
    if N<A**3:
        # ループを終了
        break
    # B=A~(10^6-1)まで
    for B in range(A,10**6):
        # (N/A)<B^2なら
        if N/A<B**2:
            # ループを終了　次のAへ
            break
        # あり得るCの数=(N/(A*B))の切り捨て-B+1
        ans+=int(N/(A*B))-B+1

# 答えの出力
print(ans)


# ---

# https://atcoder.jp/contests/abc106/tasks/abc106_b

N = int(input())

# 約数の性質として、片方が分かればもう片方もわかる
# = 全探索のt見積もりは N/2 で事足りる
# また √x という数は必ず約数の個数が奇数になるからこれの答えにはならない

ans = 0
count_divisor = 0
for i in range(1, N+1):
# 奇数以外は除外
    if i % 2 != 0:
        for j in range(1, round(i/2 + 1)):
            if i % j == 0:
                # 105: [1, 3, 5,7,15 21,35,105]
                # のように N/2の時点でN自身を除く全てが出現
                # i % j == 0がきたら count+1
                count_divisor += 1
        # j自身のみ(1で割られた時)は除外されてるから7で判定
        if count_divisor == 7:
            ans += 1
        count_divisor = 0
print(ans)
