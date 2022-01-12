# https://atcoder.jp/contests/abc234/tasks/abc234_a
#      def calc_func(t: int):
#        return (t**2) + (2 * t) + 3

#      T = int(input())
#      first = calc_func(T)
#      second = first + T
#      third = calc_func(second)
#      forth = calc_func(first)
#      last = calc_func(third + forth)
#      print(last)


# https://atcoder.jp/contests/abc234/tasks/abc234_b
# 線分の長さを求める公式は√(x2 - x1)**2 + (y2 - y1)**2
#        import math
#        N = int(input())
#        point_array = [list(map(int, input().split())) for _ in range(N)]
#        ans = 0
#        # indexが小さいものを基準点として全探索で比較
#        # ループからはみ出さないようにN-1で終了させる
#        for i in range(N):
#            for j in range(i+1, N):
#                between = math.sqrt((point_array[j][0] - point_array[i][0])**2 + (point_array[j][1] - point_array[i][1])**2)
#                ans = max(between, ans)
#        print(ans)

# https://atcoder.jp/contests/abc234/tasks/abc234_c
# 2, 20, 22, 200, 202, 220, 222, 2000, 2002, 2020, 2022, 2200, 2202, 2220, 2222
# これを二進数に変換
# 1, 10, 11, 100, 101, 110, 111, 
# そして、1,2,3...の昇順を二進数にすると
# 1, 10, 11, 100
# つまり、K番目のKを二進数に変換して、'1'となっている部分を'2'に置換すると求まる
K = int(input())
bin_K = str(bin(K))
bin_K_no_prefix = bin_K[2:]
replaced_bin_K = bin_K_no_prefix.replace('1', '2')
print(int(replaced_bin_K))
