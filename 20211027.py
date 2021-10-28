# https://atcoder.jp/contests/abc113/tasks/abc113_c

# ---------------------------------------------------

# import bisect

# n, m = map(int, input().split())
# prefecture = []
# city = []
# for i in range(m):
#     num_list = list(map(int, input().split()))
#     prefecture.append(int(num_list[0]))
#     city.append(int(num_list[1]))
# # 下6桁が小さい方が、小さいと判定される
# # 000002000001 < 000001000002 : 下6桁が優先
# sorted_country_list = sorted(set(prefecture))
# sorted_city_list = sorted(set(city))
# for index in range(m):
#     # sortされたcityの設立年(city)が何番目に大きいかを判定
#     num_index = bisect.bisect_left(sorted_city_list, city[index])
#     # id は1からスタートだから +1
#     print(str(prefecture[index]).zfill(6) + str(num_index + 1).zfill(6))

# ----------------------------------------------------


### できていること
### cityの大小関係の把握

### できていないこと
### 各県でのナンバリング

### なぜできていない
### 県関係なく大小関係でprintしているから
### 県単位で分けていない


# n, m = map(int, input().split())
# raw_list = []
# pair_dictionary = {}
# # pair_dictionary = {1: [55, 66], 2: [77]}
# # みたいなのを作りたい(最小のパフォーマンスで)
# for i in range(m):
#     # 並び順保持のためraw_listで記録
#     raw_list.append(list(map(int, input().split())))
#     prefecture_id = raw_list[i][0]
#     city_year = raw_list[i][1]
#     # 初出のpref_idをkeyとして新たにdictionaryに追加
#     if  prefecture_id in pair_dictionary:
#         # すでに定義してあるvariableをdictionaryのkeyに使う時でも、
#         # curley brackets は使わなくていい(= JSとはちがう)
#         pair_dictionary[prefecture_id].append(city_year)
#     else :
#         city_year = [city_year]
#         pair_dictionary[prefecture_id] = city_year

# # 各県内で、設立年が古い順に並べる(city)
# for pref_key in pair_dictionary:
#     pair_dictionary[pref_key].sort()

# # 下6桁が小さい方が、小さいと判定される
# # 000002000001 < 000001000002 : 下6桁が優先
# for i in range(m):
#     # sortされたcityの設立年(city)が何番目に大きいかを判定

#     # id は1からスタートだから +1
#     city_index_by_size = pair_dictionary[raw_list[i][0]].index(raw_list[i][1])
#     print(str(raw_list[i][0]).zfill(6) + str((city_index_by_size) + 1).zfill(6))

### TLEのため不正解



### 以下正解 ===========================

N, M = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(M)]
print(cities)

# 市それぞれに認識番号をつけた後、年順にソートしておく
for i in range(M):
    cities[i].append(i)
cities.sort(key=lambda x:x[1])

# 各県に割り振られた市の数を管理
id_by_pref = [0] * (N+1)

# 市（認識番号）ごとのIDを保存していくリスト
id_list = [""] * M

# 年順にソート済みなので、順番に県に割り振っていけばよい
for city in cities:
    pref, year, idx = city

    # 該当県の割り振り数を加算し、IDを作成・保存する
    id_by_pref[pref] += 1
    id = f'{pref:06}{id_by_pref[pref]:06}'
    id_list[idx] = id

# 改めて認識番号順に出力
for i in range(M):
    print(id_list[i])

