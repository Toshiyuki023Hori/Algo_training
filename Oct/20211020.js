// https://atcoder.jp/contests/abc150/tasks/abc150_
// 辞書順とは、ご想像の通り複数の文字列を比べたときに、同番目であるにも関わらず、
// a, o などと文字が違った場合、アルファベット順で「早い」方を「小さい」とする順
// -----------------
// October 19th の問題をJSで解いたもの(要はitertoolsを使わない辞書順ソート)

const permutation = ({ result = [], pre = [], post, n = post.length }) => {
  if (n > 0) {
    1

// アンダーバーのみの変数の意味はお見込みの通り
// 「単純に引数として書く必要があるため、記述はされたが特に使われていない」
// から気にしないでOKという意味です
// forEach: 1stParams => element, 2ndParams => index
    post.forEach((_, i) => {
      const rest = [...post];
      // splice(start, theNumberOfDeletedInt)
      // startで消し始めのインデックスを指定、theNumberOfDeletedIntで何個消すか指定
      const elem = rest.splice(i, 1);
      console.log(elem)
      permutation({ result, pre: [...pre, ...elem], post: rest, n: n - 1});
    });
  } else {
    result.push(pre);
  }
  return result;
};

const array = [0, 1, 2, 3];
const results = permutation({ post: array });
console.log(results);

const results2 = permutation({ post: array, n: 2 });
console.log(results2);