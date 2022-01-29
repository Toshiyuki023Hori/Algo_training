# https://atcoder.jp/contests/abc114/tasks/abc114_c
# 再起関数の練習
N = int(input())

def func(current, use, counter):
  if current > N: return
  if use == 0b111: counter.append(1)  # 答えを増やす

  # 7を付け加える
  func(current * 10 + 7, use | 0b001, counter)
  # 5を付け加える
  func(current * 10 + 5, use | 0b010, counter)
  # 3を付け加える
  func(current * 10 + 3, use | 0b100, counter)

res = []
func(0, 0, res)
print(sum(res))
