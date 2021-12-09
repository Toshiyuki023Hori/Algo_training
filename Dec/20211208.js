// https://atcoder.jp/contests/abc213/tasks/abc213_c
// 復習

// 考え方としては下記参照
// https://algo-logic.info/coordinate-compress/
/*
1. X軸の一列を座圧
2. Y軸の一列を座圧


*/

// このコードは不正解
function main(input) {
  let inputArray = input.split("\n");
  const [H, W, N] = inputArray[0].split(" ");
  // 改行で 1 index分余計にarrayに入ってる
  inputArray.pop();
  // input_arrayには、HWNのindexも入ってるから、その分 -1
  let y_array = [];
  let x_array = [];
  for (let i = 0; i < inputArray.length - 1; i++) {
    dividedRaw = inputArray[i + 1].split(" ");
    y_array.push(parseInt(dividedRaw[0], 10));
    x_array.push(parseInt(dividedRaw[1], 10));
  }
  // JSのsort()は破壊的(元のarrayを変更する)なので、
  // slice()をかまして、新しいarrayを生成、それにsort()を実行
  let y_set = new Set(y_array);
  let x_set = new Set(x_array);
  let sorted_y_array = Array.from(y_set).slice().sort();
  let sorted_x_array = Array.from(x_set).slice().sort();
 
  let ans = "";
  for (let i = 0; i <= N-1; i++) {
    // 知りたいのは、y_array(x_array)内において、array[i]がどれほど大きいか
    let sizeOf_y = sorted_y_array.indexOf(y_array[i]) + 1;
    let sizeOf_x = sorted_x_array.indexOf(x_array[i]) + 1;
    ans += `${sizeOf_y} ${sizeOf_x}`;
    if (i !== N - 1) {
      ans += "\n";
    }
  }
  console.log(ans);
}
 
main(require("fs").readFileSync("/dev/stdin", "utf8"));
