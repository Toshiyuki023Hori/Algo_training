# https://atcoder.jp/contests/abc079/tasks/abc079_c
# bit全探索の練習

# おそらく operator のところをbit全探索する
# 0 -> '-'
# 1 -> '+'
# 000 => A - B - C - D
# 010 => A - B + C - D

# 全通り数としては、2**3 = 12 通り
Num = input()
NumList = [int(Num[i]) for i in range(4)]
operator = ''
# range => 0~7
# 2進数で言えば、0b001 ~ 0b111
    # ここで '+' と '-' をパワープレイで当てはめる
    # --- : 0
    # --+ : 1
    # -+- : 2
    # -++ : 3
    # +-- : 4
    # +-+ : 5
    # ++- : 6
    # +++ : 7
# 上記 0 - 7を試すためにrange(2 ** 3 = 8)
def ex_cal(ope, num_list, index):
    ans = 0
    if ope[index] == '+':
        ans = num_list[i] + num_list[i+1]
    if ope[index] == '-':
        ans = num_list[i] - num_list[i+1]
    return ans
for i in range(2 ** 3):
    # 等号が入る箇所は3箇所だからrange(3) -> index: 0, 1, 2
    for j in range(3):
        # i >> j & 1 が Trueの時 = + フラグが立つ
        if i >> j & 1:
            operator = '+' + operator
        elif not i >> j & 1:
            operator = '-' + operator
    # operandに対応した計算を実行
    sum = 0
    for i in range(len(operator)):
        if i == 0:
            sum += ex_cal(operator, NumList, i)
        elif i == 1:
            sum += ex_cal(operator, NumList, i)
        elif i == 2:
            sum += ex_cal(operator, NumList, i)
    print(str(NumList[0]) + operator[0] + str(NumList[1]) + operator[1] + str(NumList[2]) + operator[2] + str(NumList[3]) + '=' + str(sum))
    if sum == 7:
        print(str(NumList[0]) + operator[0] + str(NumList[1]) + operator[1] + str(NumList[2]) + operator[2] + str(NumList[3]) + '=' + str(sum))
        exit
    operator = ''


### 以下、正解のコード(上のワシのやつと正解を合わせた)

Num = input()
NumList = [int(Num[i]) for i in range(4)]
operator = ''

for i in range(2 ** 3):
    total = NumList[0]
    ans = str(NumList[0])
    # 等号が入る箇所は3箇所だからrange(3) -> index: 0, 1, 2
    for j in range(3):
        # i >> j & 1 が Trueの時 = + フラグが立つ
        if i >> j & 1:
            total += NumList[j + 1]
            ans += '+'
        elif not i >> j & 1:
            total -= NumList[j + 1]
            ans += '-'
        ans += str(NumList[j + 1])
    if total == 7:
        break
print(ans + '=7')
