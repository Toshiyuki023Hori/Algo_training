# https://atcoder.jp/contests/abc201/tasks/abc201_c
# これは解けなかった問題です
# 解説見ながら自分でコード書いた感じ
# 4桁の暗証番号なので、10**4 = 10,000通りなので十分全探索できる
def judge(s, must_array, error_array) :
    for o in must_array:
        # oはsに確実に含まれています
        if o not in s:
           return False
    for x in error_array:
        # xはsに確実に含まれていません
        if x in s:
           return False
    return True

S = input()

# 絶対に入っているリストと絶対に含まれていないリストを作る
must_nums = []
error_nums = []

for idx, char in enumerate(S):
    if char == 'o' :
        must_nums.append(str(idx))
    elif char == 'x' :
        error_nums.append(str(idx))

ans = 0
# 0000 ~ 9999を生成
for i in range(10000):
    s = str(i).zfill(4)
    if judge(s, must_nums, error_nums) :
        ans += 1
print(ans)

