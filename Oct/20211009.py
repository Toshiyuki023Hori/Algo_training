# https://atcoder.jp/contests/abc222/tasks/abc222_a

n = input()
oneZero = '0'
twoZeros = '00'
threeZeros = '000'

if len(n) == 1:
    n = threeZeros + n
if len(n) == 2:
    n = twoZeros + n
if len(n) == 3:
    n = oneZero + n
print(n)

# https://atcoder.jp/contests/abc222/tasks/abc222_b
n, p = map(int, input().split(' '))
score_array = input().split(' ')
count = 0
# 生徒1人の条件分岐
if n == 1:
    if int(score_array[0]) >= p:
        print(count)
    else :
        print(count + 1)
if n >= 2:
    for score in score_array:
        if int(score) < p:
            count += 1
print(count)

# https://atcoder.jp/contests/abs/tasks/abc085_b
number_of_mochi = input()
# 全部のモチを一つの配列に格納
mochi_array = [int(input()) for raw in range(int(number_of_mochi))]
mochi_array.sort()
floors = 1
for i in range(len(mochi_array)):
        if i > 0 and mochi_array[i] > mochi_array[i - 1]:
            floors += 1
print(floors)