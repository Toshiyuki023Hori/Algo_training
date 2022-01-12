# https://atcoder.jp/contests/abc231/tasks/abc231_c
import bisect
N, Q = map(int, input().split(' '))
height_list = list(map(int, input().split()))
# 元のarrayの順番を変更
height_list.sort()
# 問われる身長をarrayにまとめて保存
question_list = [int(input()) for _ in range(Q)]
for i in range(Q):
    # 10**9というのが最大数列なので、まともに全探索すると制限を超えると想像
    # 整列したarrayで条件を満たす最初のindexを取得 -> sortされているので順列のlengthからindexを引いてやる
    first_index = bisect.bisect_left(height_list, question_list[i])
    # あくまでもindexで表した数にこだわりたいので、N-1とする
    print((N-1) - first_index + 1)

# 一発クリア、以下結果
# ケース名	実行時間
# case_00.txt>  431 ms
# case_01.txt	405 ms
# case_02.txt	409 ms
# case_03.txt	406 ms
# case_04.txt	408 ms
# case_05.txt	303 ms
# case_06.txt	297 ms
# case_07.txt	267 ms
# case_08.txt	214 ms
# case_09.txt	393 ms
# case_10.txt	309 ms
# case_11.txt	227 ms
# case_12.txt	187 ms
# case_13.txt	337 ms
# case_14.txt	279 ms
# case_15.txt	280 ms
# case_16.txt	335 ms
# sample_00.txt	  50 ms
# sample_01.txt	  50 ms
# sample_02.txt	  47 ms
