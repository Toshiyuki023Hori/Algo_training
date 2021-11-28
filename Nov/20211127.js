function main(input) {
  const input_array = input.split(" ");
  const a = input_array[0];
  // JSの場合、Atcoderの標準出力の最後の改行も拾うから注意
  // Ex) 入力が下記の場合
  // '2342342 34242342
  // (末に改行入ってる)'
  // input().split(' ')をすると、後ろの数字は
  // '3424342
  // (改行)'
  // というように改行が入るので、それを取り除く処理を書かなければいけない
  let b = input_array[1].split("\n");
  b = b[0];
  const min_len = Math.min(a.length, b.length);
  let isHard = false;
  for (let i = 1; i <= min_len + 1; i++) {
    if (parseInt(a[a.length - i], 10) + parseInt(b[b.length - i], 10) >= 10) {
      console.log("Hard");
      isHard = true;
      break;
    }
  }
  if (!isHard) {
    console.log("Easy");
  }
}

main(require("fs").readFileSync("/dev/stdin", "utf8"));
