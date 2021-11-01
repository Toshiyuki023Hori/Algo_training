# LeetCode Roman To Integer(https://leetcode.com/problems/roman-to-integer/)

class Solution:
    def romanToInt(self, s: str) -> int:
        sumNum = 0
        for i in range(0, len(s)):
            if s[i] == 'I':
                sumNum += 1
            if s[i] == 'V':
                sumNum += 5
            if s[i] == 'X':
                sumNum += 10
            if s[i] == 'L':
                sumNum += 50
            if s[i] == 'C':
                sumNum += 100
            if s[i] == 'D':
                sumNum += 500
            if s[i] == 'M':
                sumNum += 1000
            if i > 0:
                # 前が 'I', 'X', 'C'ならその倍数引く(足した分を割引くため)
                if s[i] != 'I' and s[i-1] == 'I':
                    sumNum -= 2
                if s[i] != 'X' and s[i-1] == 'X':
                    sumNum -= 100
                if s[i] != 'C' and s[i-1] == 'C':
                    sumNum -= 200
        return sumNum
    


# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000


# atcoder https://atcoder.jp/contests/abc220/tasks/abc220_a

# b/c の余りを切り捨てた数(X)
# 上記 X に c をかけた数(Y)
# このYは、b以下のcの最大の倍数であり、故に Y >= A が成り立てばこのアルゴリズムは解ける

a, b, c = map(int, input().split(' '))
# pythonでは // で切り捨て割り算ができる
x = b // c
y = x * c
if x * c >= a:
    print(y)
else :
    print('-1')