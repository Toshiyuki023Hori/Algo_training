# https://atcoder.jp/contests/abc175/tasks/abc175_b
n = int(input())

# 棒の長さのリスト
A = list(map(int, input().split()))
A.sort()

# 条件を満たす三角形の数
ans = 0

for i in range(n-2):
    for j in range(i,n-1):
        if A[i] == A[j]: # 長さが等しければスキップ
            continue
        for k in range(j,n):
            if A[j] == A[k]: # 長さが等しければスキップ
                continue
            if A[i]+A[j]>A[k]: # 三角形として成立しているか判定
                ans += 1

print(ans)
