# https://atcoder.jp/contests/abc226/tasks/abc226_a
import decimal
x = input()
print(decimal.Decimal(x).quantize(decimal.Decimal('0'), rounding=decimal.ROUND_HALF_UP))


# https://atcoder.jp/contests/abc226/tasks/abc226_b
# n = int(input())
# count = 0
# all_array = []
# for i in range(n):
#     temp_input = list(map(int, input().split()))
#     # len_array = temp_input[:1]
#     temp_array = temp_input[1:]
#     if not temp_array in all_array:
#         count += 1
#     all_array.append(temp_array)
# print(count)

n = int(input())
all_array = []
for i in range(n):
    temp_input = tuple(map(int, input().split()))
    # len_array = temp_input[:1]
    temp_array = temp_input[1:]
    all_array.append(temp_array)
all_set = set(all_array)
print(all_set)
