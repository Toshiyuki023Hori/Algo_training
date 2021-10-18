# Beginner Contest 223 https://atcoder.jp/contests/abc223/tasks

# A: Extra Price
a = int(input())
if a < 100 or a % 100 != 0:
    print('No')
elif a % 100 == 0:
    print('Yes')

# C: Doukasen
# 1. 上の導火線が1秒でどれだけいくか計算
# 2. 下の導火線が1秒でどれだけいくか計算
# 3. これを繰り返す

n = input().split(' ')
# n => ['n'] : list
doukasen = []
for row in range(int(n[0])):
    row_num = input().split('\n')
    # row_num => ['a b']
    doukasen.append(row_num[0].split(' '))
    # doukasen => [['a1', 'b1'], ['a2', 'b2']]
print(doukasen)

# step1
rest_cm = 0
rest_sec = 0
for i in range(len(doukasen)):
    rest_sec = doukasen[i][0] / doukasen[i][1]
    



# Step1
