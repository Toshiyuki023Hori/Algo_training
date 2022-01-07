grid = [input().split('\n')  for i in range(2)]
if grid[0][0][0] == '#' and grid[0][0][1] == '.' and grid[1][0][0] == '.' and grid[1][0][1] == '#':
    print('No')
elif grid[0][0][0] == '.' and grid[0][0][1] == '#' and grid[1][0][0] == '#' and grid[1][0][1] == '.':
    print('No')
else :
    print('Yes')


# https://atcoder.jp/contests/abc229/tasks/abc229_b
A, B = map(str, input().split(' '))
# 数が小さい方の桁に合わせる
for i in reversed(min(len(A), len(B))):
    if int(A[i]) + int(B[i]) > 9:
        print('Hard')
        break
print('Easy')

