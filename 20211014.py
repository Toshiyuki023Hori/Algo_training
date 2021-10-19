# atcoder(https://atcoder.jp/contests/abc120/tasks/abc120_b)

import math
a,b,k = map(int, input().split(' '))
# 最大公約数を抽出
greatest_common_divisor = math.gcd(a, b)
 
def make_divisors(n):
    # 小さい方からの列挙、大きい方からの列挙で別のlistを作成
    lower_divisors , upper_divisors = [], []
    i = 1
    # なぜ二乗以下で約数が全て求められるのか(https://algo-method.com/descriptions/84)
    # 約数の性質として、一つ見つかれば対で約数がもう一つ見つかるというものがある
    # Ex) 36 / 2 = 18 => divisor: 2 & 18
    # ここで√nが整数となる数を考える
    # 36の場合、√36 = 6 となる
    # これを上記約数の性質で当てはめると、対となる約数は同じ数となる
    # すなわち √n 以下の数を調べるだけで、約数は全て調べられることになる
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            ## '//'は余りを切り捨てた割り算
            ## √n が整数でなければ対で求められた割り算の結果をappend
            if i != n // i:
              upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
 
divisor_list = make_divisors(greatest_common_divisor)
print(divisor_list[-k])

# 最大公約数は、ユークリッドの互除法を使って解くこともできるから、
# python でのその処理の書き方はまた別途調べてください