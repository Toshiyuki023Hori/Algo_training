function main(input) {
    let input = input.split('\n');
    input = input[0]
    console.log(input)
    const basic_str = 'oxx'
    let T;
    for (let i = 0; i <= 8; i++){
        T += basic_str;
    }
    const res = basic_str.search(input);
    console.log(res === -1 ? 'No' : 'Yes');
  }
  
  main(require("fs").readFileSync("/dev/stdin", "utf8"));
