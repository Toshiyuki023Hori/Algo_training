# https://atcoder.jp/contests/abc113/tasks/abc113_c


import bisect

n, m = map(int, input().split())
country = []
city = []
for i in range(m):
    num_list = list(map(int, input().split()))
    country.append(int(num_list[0]))
    city.append(int(num_list[1]))
# 下6桁が小さい方が、小さいと判定される
# 000002000001 < 000001000002 : 下6桁が優先
sorted_country_list = sorted(set(country), reverse=True)
sorted_city_list = sorted(set(city), reverse=True)
for city_num in sorted_city_list:
    num_index = bisect.bisect_left(city, city_num)
    country_id = str(country[num_index])
    print(country_id.zfill(6) + str(city_num).zfill(6))




