# https://atcoder.jp/contests/abc095/tasks/arc096_a
# 全探索だが、値が一意に絞り込めるものに関してはループさせず、パフォーマンスを上げる

a_price, b_price, mix_price, a_slices, b_slices = map(int, input().split())

# 1e5 みたいなのを"数値リテラル"という
min_price = 2 * 5000 * int(1e5)
# a + b < 2 mix => a, bを一枚ずつ買う方がお得
# a + b > 2 mix => mixを二枚買う方がお得

# a_slicesとb_slicesの数の小さい枚数分でmixを買う
# これはmixを多めに買ってしまうと、①mixで買い足した金額、②a, 若しくはbを足りない分だけ単品で買い足した金額
# で比較ができないから
# 多めに買う分には問題ないので、例えば a_slices > b_slicesの場合、a_slices - b_slicesというのは、
# mixか単品どちらで買うのが安いかを比較するために使われる

# ただし、この方法は枝刈り全探索とは違う

# mix が割高パターン
if a_price + b_price <= 2 * mix_price:
    print(a_price * a_slices + b_price * b_slices)
else:
    if a_slices >= b_slices:
        mix_sum = 2 * mix_price * b_slices
        left_slices = a_slices - b_slices
        print(min(2 * mix_price * a_slices, mix_sum + a_price * left_slices))
    else :
        mix_sum = 2 * mix_price * a_slices
        left_slices = b_slices - a_slices
        print(min(2 * mix_price * b_slices, mix_sum + b_price * left_slices))


# ==== 
# 下記が枝刈り全探索ver
# ====

# 金額A,B,Cのパターン全探索すると時間がかかる。ABCXYを数式化してみよう。ABピザの枚数をZ枚として、、、
# A(X-Z)+B(Y-Z)+2CZ
# 2CZ=AZ+BZなのでAXとBYから引いてあげれば帳尻が合う。

A, B, C, X, Y = map(int, input().split())
ans = 2*(5000*10**5)
for Z in range(10**5+1):
    total = A*max(X-Z, 0)+B*max(Y-Z, 0)+2*C*Z
    ans = min(total,ans)
print(ans)

