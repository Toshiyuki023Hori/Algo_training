# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_c
# 考え方としてはabc201_cが参考になるかも

foods = {
            'onigiri' : 100,
            'sand' : 101,
            'cookie' : 102,
            'cake' : 103,
            'candy' : 104,
            'pc' : 105
        }

# 100,000 / 100 = 1,000通り
# 一番小さい100からあまりを順に見ていけばいい
# quan_sand = int(X / 101)
# quan_cookie = int(X / 102)
# quan_cake = int(X / 103)
# quan_candy = int(X / 104) 
# quan_pc = int(X / 105)

def return_one_or_zero():
    X = int(input())
    quan_onigiri = int(X / 100) 
    left_X = X
    for o in range(quan_onigiri, 0, -1) :
        if left_X == 100 * o :
            return 1
        else :
            left_X = left_X - 100 * o
            for s in range(int(left_X / 101), 0, -1) :
                if left_X == 101 * s :
                    return 1
                else :
                    left_X = left_X - 101 * s
                    for ckie in range(int(left_X / 102), 0, -1) :
                        if left_X == 102 * ckie :
                            return 1
                        else :
                            left_X = left_X - 102 * ckie
                            for cke in range(int(left_X / 103), 0, -1) :
                                if left_X == 103 * cke :
                                    return 1
                                else : 
                                    left_X = left_X - 103 * cke
                                    for cnd in range(int(left_X / 104), 0, -1) :
                                        if left_X == 104 * cnd :
                                            return 1
                                        else :
                                            left_X = left_X - 104 * cnd
                                            for p in range(int(left_X / 105), 0, -1) :
                                                if left_X == 105 * p :
                                                    return 1
                    return 0
        
print(return_one_or_zero())

    

        
