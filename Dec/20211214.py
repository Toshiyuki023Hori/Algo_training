# https://atcoder.jp/contests/abc150/tasks/abc150_c

# 想定される最大の通り数は8!通り = 40,320通り < Atcoderの最大の見積もり100,000よりも少ない

import itertools
N = int(input())
# mapは、map(func, iterable)で構成されており、
# iterableの各要素にfuncの処理を行う
# 尚、paramはimplicitに渡されているので、func実行時のparentasesはいらない
P_ARRAY = list(map(int, input().split()))
Q_ARRAY = list(map(int, input().split()))

N_ARRAY = [int(i+1) for i in range(N)]
N_PERMUTATIONS = list(itertools.permutations(N_ARRAY, N))

p_num = 0
q_num = 0

for i in range(len(N_PERMUTATIONS)):
    # Pythonにおいて、Arrayを並びも完全に一致しているか調べたい時、
    # list1 == list2 
    # とする
    # permutationsの各elementはsetなので、それをlistに変換(じゃないと == でTrueと判断してくれない)
    if P_ARRAY == list(N_PERMUTATIONS[i]):
        p_num = i
    if Q_ARRAY == list(N_PERMUTATIONS[i]):
        q_num = i
print(abs(p_num - q_num))


