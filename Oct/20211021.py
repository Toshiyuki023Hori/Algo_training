# https://atcoder.jp/contests/abc212/tasks/abc212_b

### 一個だけWrong Answerになる... なぜ?
### range(3)にして、i + 2 をやめたら通った
s = input()
isStrong = True
for i in range(3):
    if len(set(s)) == 1:
        isStrong = False
        break
    if (int(s[i]) + 1 ) % 10 == (int(s[i + 1])) % 10:
        isStrong = False
    else:
        isStrong = True
        break
if isStrong:
  print('Strong')
else :
  print('Weak')

### 
A = list(map(int, input()))

if len(set(A)) == 1 or all((A[i] + 1) % 10 == A[i + 1] % 10 for i in range(3)):
    print("Weak")
else:
    print("Strong")
