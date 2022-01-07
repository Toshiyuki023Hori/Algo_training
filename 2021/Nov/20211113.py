# Beginner Contest227

N, K, A = map(int, input().split())
all_num = [int(i) for i in range(1, N + 1)]
list_index = A - 1
i = 1
while i != K:
    target = all_num[list_index]
    if (list_index == N - 1):
        list_index = 0
    else :
        list_index += 1
    i += 1
print(all_num[list_index])


