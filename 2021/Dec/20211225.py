# https://atcoder.jp/contests/abc233/tasks/abc233_a

        # X, Y = map(int, input().split(' '))
        #
        # count = 0
        # price = X
        # while price < Y:
        #     price += 10
        #     count += 1
        # print(count)


#############################################################
# https://atcoder.jp/contests/abc233/tasks/abc233_b

        # L, R = map(int, input().split(' '))
        # S = input()
        # start = S[:L-1]
        # target = S[L-1:R]
        # end = S[R:]
        # reversed_target = target[len(target)::-1]
        # print(start + reversed_target + end)

#############################################################
# https://atcoder.jp/contests/abc233/tasks/abc233_c

N, X = map(int, input().split(' '))
how_many_lists = []
nums_lists = []
for i in range(N):
    raw_one_row = list(map(int, input().split(' ')))
    how_many_lists.append(raw_one_row[0])
    raw_one_row.pop(0)
    nums_lists.append(raw_one_row)

# 要はL1 * L2 * L3 通り考えられる
# 10**5を超えそう
ans = 0






