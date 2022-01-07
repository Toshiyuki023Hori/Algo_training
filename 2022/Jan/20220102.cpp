// https://atcoder.jp/contests/abc175/tasks/abc175_b
#include "bits/stdc++.h"
using namespace std;

int main() {
  int N;
  cin >> N;
  vector<int> nums_array(N);
  for (int i = 0; i < N; i++) {
    cin >> nums_array[i];
  }
  set<int> unique_nums_set(nums_array.begin(), nums_array.end());
  // この時点で昇順に並び替えされてる
  vector<int> unique_nums_array(unique_nums_set.begin(), unique_nums_set.end());

  // C++ の sizeofはbyte数を出力する
  // unique_nums_array[0]は配列要素の型サイズを出力する
  // したがって下の式は配列全体のバイト数sizeof(ary)を配列要素の型サイズsizeof(int)で割っていると言える
  for (int num : unique_nums_array) {
    cout << num;
  }
  int len = sizeof(unique_nums_array) / sizeof(unique_nums_array[0]);
  // このdo~whileで順列を全て列挙している
  // 1. next_permutationで順列が辞書順で列挙
  // 2. 各順列ごとに行う処理をdo{}内で実行
  // 下の場合、長さlenの順列に対して処理を行たい
  // 4 5 9 7 8 1
  // 4 5 9 8 1 7
  // みたいに配列要素の場合、当然各要素に対する処理はindexが必要なので、forループを使う必要がある
  ////// array of array
  //////を作るときは、下のように中に入るarrayのdatatypeも指定する必要がある
  vector<vector<int>> perumutated_array;
  do {
    perumutated_array.push_back(unique_nums_array);
  } while (
      next_permutation(unique_nums_array.begin(), unique_nums_array.end()));
  for (vector<int> row : perumutated_array) {
    for (int i = 0; i < row.size(); i++) {
      cout << row[i] << " ";
    }
    cout << endl;
  }
}
