# https://atcoder.jp/contests/abc215/tasks/abc215_b
# ANSWER
n = int(input())
if n == 1:
    print(0)
else :
    # N <=10^18 なので ｋは最大で60程度の値になります。
    for i in range(100):
        # pow(base, exp[, mod])
        # base の exp 乗を返します
        if pow(2, i) <= n:
            continue
        # nを超えた瞬間にprint
        else :
            print(i - 1)
            break