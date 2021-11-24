// https://atcoder.jp/contests/abc095/tasks/arc096_a

function Main(input) {
  const numArray = input.split(" ");
  const A = parseInt(numArray[0], 10);
  const B = parseInt(numArray[1], 10);
  const C = parseInt(numArray[2], 10);
  const X = parseInt(numArray[3], 10);
  const Y = parseInt(numArray[4], 10);

  // 出来うる限り大きい値に設定
  let minPrice = C * 10e6;

  //   A + B > 2C の場合、少ない方の枚数までは2Cで買う方がいい(多い方 - 少ない方は比較)
  //   A + B < 2C の場合、それぞれで買った方が安い
  let ans;
  if (A + B < 2 * C) {
    const aSum = A * X;
    const bSum = B * Y;
    ans = aSum + bSum;
  } else if (A + B >= 2 * C) {
    // XとY少ない方の枚数をまず購入する
    // 多い方 - 少ない方の数をA, Bでそれぞれ買ったパターン、Cで買ったパターンで比較
    let sum;
    if (X >= Y) {
      sum = 2 * C * Y;
      const leftPurchase = X - Y;
      sum += Math.min(A * leftPurchase, 2 * C * leftPurchase);
    } else if (X <= Y) {
      sum = 2 * C * X;
      const leftPurchase = Y - X;
      sum += Math.min(B * leftPurchase, 2 * C * leftPurchase);
    }
    ans = sum;
  }
  if (minPrice > ans) {
    minPrice = ans;
  }
  console.log(minPrice);
}
Main(require("fs").readFileSync("/dev/stdin", "utf8"));
