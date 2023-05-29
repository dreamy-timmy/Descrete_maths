# Крускалы
# I = {1,2,3,4,5,6,7}
# ribs = [[1,2], [1,4], [1,5], [1,6], [2,3], [2,4], [2,5], [2,6],
#         [2,7], [3,5], [3,7], [4,5], [4,6], [4,7], [5,6], [5,7], [6,7]]
# weight = [4, 3, 6, 1, 2, 3, 7, 6, 1, 4, 2, 1, 5, 3, 3, 6, 7]
# current = [i for i in weight]
# sm = 0
# tops = set()
# sm += min(weight)
# tops.add(ribs[weight.index(min(weight))][0])
# tops.add(ribs[weight.index(min(weight))][1])
# ribs.remove(ribs[weight.index(min(weight))])
# weight.remove(min(weight))
# while weight:
#     ind = f = c = 0
#     for i in range(len(ribs)):
#         if (ribs[i][0] in tops or ribs[i][1] in tops) and not(ribs[i][0] in tops and ribs[i][1] in tops):
#             if c == 0:
#                 ind = i
#                 c = 1
#             if weight[i] < weight[ind]:
#                 ind = i
#                 c = 1
#     sm += weight[ind]
#     tops.add(ribs[ind][0])
#     tops.add(ribs[ind][1])
#     weight.pop(ind)
#     ribs.pop(ind)
#     if I == tops: break
# print(sm)


# Прима
# I = {1,2,3,4,5,6,7}
# ribs = [[1,2], [1,4], [1,5], [1,6], [2,3], [2,4], [2,5], [2,6],
#         [2,7], [3,5], [3,7], [4,5], [4,6], [4,7], [5,6], [5,7], [6,7]]
# weight = [4, 3, 6, 1, 2, 3, 7, 6, 1, 4, 2, 1, 5, 3, 3, 6, 7]
# current = [i for i in weight]
# sm = 0
# tops = set()
# tops.add(ribs[0][0])
# while(weight):
#     mn_i = 0
#     trash = 0
#     f = f1 = 0
#     for i in range(len(weight)):
#         if ribs[i][0] in tops and ribs[i][1] in tops:
#             trash = i
#             f1 = 1
#             break
#     if f1 == 1:
#         weight.pop(trash)
#         ribs.pop(trash)
#     for i in range(len(weight)):
#         if (ribs[i][0] in tops or ribs[i][1] in tops) and (ribs[i][0] not in tops or ribs[i][1] not in tops):
#             if weight[i] <= weight[mn_i]:
#                 f = 1
#                 mn_i = i
#     if f:
#         tops.add(ribs[mn_i][0])
#         tops.add(ribs[mn_i][1])
#         sm += weight[mn_i]
#         weight.pop(mn_i)
#         ribs.pop(mn_i)
#     if tops == I: break
# print(sm)

# Дейкстра
# I = [1,2,3,4,5,6,7,8,9,10,11,12]
# ribs = [[1,2], [1,5], [1,6], [2,3], [2,4], [2,5], [2,6], [3,4],
#         [3,5], [4,5], [4,7], [4,8], [5,6], [5,7], [5,8], [5,9],
#         [6,8], [6,9], [7,8],[7,10], [7,11], [8,9], [8,10], [8,11], [8,12],
#         [9,11], [9,12], [10,11], [11,12]]
# weight = [7, 9, 2, 5, 4, 8, 2, 2, 9, 3, 8, 3, 3, 5, 1, 7, 6, 1, 6, 4, 4, 2, 7, 8, 5, 6, 1, 10, 3]
# tops = set()
# sm = 0
# s = [None for i in range(len(I))]
# tops.add(I[0])
# s[I[0]-1] = 0
# current = []
# top = 1
# ind = -1
# delete = []
# f = 1
# while ribs:
#         if ind + 1 <= len(ribs)-1: ind += 1
#         else:
#             if current:
#                 mn = s[current[0] - 1]
#                 t = current[0]
#                 for j in range(len(current)):
#                     if mn > s[current[j] - 1]:
#                         t = current[j]
#                         mn = s[current[j] - 1]
#                 tops.add(t)
#                 top = t
#                 current = []
#                 ind = 0
#                 delete.sort(reverse=1)
#                 while delete:
#                     ribs.pop(delete[0])
#                     weight.pop(delete[0])
#                     delete.pop(0)
#             else:
#                 for i in range(len(I)):
#                     if I[i] not in tops:
#                         top = I[i]
#                         tops.add(top)
#                         break
#         if weight and top == ribs[ind][0] and f:
#             if s[ribs[ind][1] - 1]:
#                     s[ribs[ind][1]-1] = min(s[ribs[ind][0]-1] + weight[ind], s[ribs[ind][1]-1])
#             else:
#                     s[ribs[ind][1]-1] = s[ribs[ind][0]-1] + weight[ind]
#             current.append(ribs[ind][1])
#             delete.append(ind)
#         elif weight and top == ribs[ind][1] and f:
#             if s[ribs[ind][0] - 1]:
#                     s[ribs[ind][0]-1] = min(s[ribs[ind][1]-1] + weight[ind], s[ribs[ind][0]-1])
#             else:
#                     s[ribs[ind][0]-1] = s[ribs[ind][1]-1] + weight[ind]
#             current.append(ribs[ind][0])
#             delete.append(ind)
# print(s)

# #алгоритм Флойда
# I = {1,2,3,4,5,6}
# r = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],
#     [2,1],[2,2],[2,3],[2,4],[2,5],[2,6],
#      [3,1],[3,2],[3,3],[3,4],[3,5],[3,6],
#      [4,1],[4,2],[4,3],[4,4],[4,5],[4,6],
#      [5,1],[5,2],[5,3],[5,4],[5,5],[5,6],
#      [6,1],[6,2],[6,3],[6,4],[6,5],[6,6]]
# w = [0,1,100,100,6,3,
#      1,0,6,100,100,5,
#      100,6,0,1,3,3,
#      100,100,1,0,2,100,
#      6,100,3,2,0,4,
#      3,5,3,100,4,0]
# for top in I:
#     for i in I:
#         for j in I:
#             w[r.index([i,j])] = min(w[r.index([i,top])] + w[r.index([top,j])],w[r.index([i,j])])
# #красивый вывод табличкой
# for i in I:
#     s = ''
#     for j in I:
#         s += str(w[r.index([i,j])])+' '
#     print(s)

# алгоритм Форда-Беллмана
# n = 5
# C = [[None,1,None,None,3],
#     [None,None,8,7,1],
#     [None,None,None,1,-5],
#     [None,None,2,None,None],
#     [None,None,None,4,None]]
# lam = [[None for j in range(n)] for i in range(n)]
# begin = 3-1 #начальная вершина-1
# for i in range(n): lam[i][begin] = 0
# print(lam)
# for i in range(1,n):
#     for j in range(n):
#         if j != begin:
#             comparing = []
#             for k in range(n):
#                 if lam[i-1][k] != None and C[k][j] != None:
#                     comparing.append(lam[i-1][k] + C[k][j])
#             if comparing:
#                 lam[i][j] = min(comparing)
#         if i != 0 and j == n-1:
#             if lam[i - 1][j] == lam[i][j]: break
# # путь из вершины 1 в остальные:
# print(lam[-1])


# # метод ветвей и границ (всегда идём, не сравнивая)
# # сделать через "*", помечая все те, что мы типа удалили
# import math
# def f(C,road,ans):
#     sm = 0
#     d = ()
#     for i in range(len(C)):
#         for j in range(len(C[i])):
#             if C[i][j] == 0:
#                 one = [C[k][j] for k in range(len(C[j])) if str(C[k][j]).isdigit() and k != i]
#                 two = [C[i][k] for k in range(len(C[i])) if str(C[i][k]).isdigit() and k != j]
#                 if one: mn1 = min(one)
#                 else: mn1 = math.inf
#                 if two: mn2 = min(two)
#                 else: mn2 = math.inf
#                 if (mn1 + mn2) > sm: d = (i, j)
#                 sm = max(mn1 + mn2, sm)
#     ans.append((d[0],d[1]))
#     for i in range(len(C)):
#         for j in range(len(C[i])):
#             if j == d[1] or i == d[0]: C[i][j] = "*"
#     for i in range(len(C)):
#         for j in range(len(C[i])):
#             if i == d[1] and j == d[0]:
#                 C[i][j] = math.inf
#     for i in range(len(C)):
#         thing = [C[i][j] for j in range(len(C[i])) if str(C[i][j]).isdigit()]
#         if thing:
#             mn = min(thing)
#             road += mn
#             for j in range(len(C[i])):
#                 if str(C[i][j]).isdigit(): C[i][j] -= mn
#     for j in range(len(C)):
#         thing = [C[i][j] for i in range(len(C)) if str(C[i][j]).isdigit()]
#         if thing:
#             mn = min(thing)
#             road += mn
#             for i in range(len(C)):
#                 if str(C[i][j]).isdigit(): C[i][j] -= mn
#     return C,road,ans
# C = [[math.inf,12,22,28,32],
#     [12,math.inf,10,40,20],
#     [22,10,math.inf,50,10],
#     [28,27,17,math.inf,27],
#     [32,20,10,60,math.inf]]
# # ищем корень
# root = 0
# for i in range(len(C)):
#     mn = min(C[i][j] for j in range(len(C[i])) if C[i][j] != None)
#     root += mn
#     for j in range(len(C[i])):
#         if C[i][j] != None: C[i][j] -= mn
# for j in range(len(C)):
#     mn = min(C[i][j] for i in range(len(C)) if C[i][j] != None)
#     root += mn
#     for i in range(len(C)):
#         if C[i][j] != None: C[i][j] -= mn
# d = ()
# value = []
# sm = 0
# road = root
# while any(str(C[i][j]).isdigit() for i in range(len(C)) for j in range(len(C[i]))):
#     one = f(C, road, value)
#     C = one[0]
#     road = one[1]
# print(value)
# print(road)

# Форд-Фалкерсон
# import math
# # чисто формально написал вершины
# I = [1,2,3,4,5,6,7,8]
# C = [[math.inf,95,math.inf,math.inf,75,32,57,math.inf],
#     [math.inf,math.inf,6,math.inf,18,math.inf,math.inf,math.inf],
#     [math.inf,math.inf,math.inf,7,math.inf,math.inf,11,math.inf],
#     [math.inf,math.inf,math.inf,math.inf,math.inf,math.inf,math.inf,81],
#     [math.inf,math.inf,9,math.inf,math.inf,math.inf,24,math.inf],
#     [math.inf,5,math.inf,math.inf,math.inf,math.inf,20,16],
#     [math.inf,math.inf,math.inf,20,math.inf,math.inf,math.inf,94],
#     [math.inf,math.inf,math.inf,math.inf,math.inf,math.inf,math.inf,math.inf]
# ]
# sm = 0
# mn = 0
# trash = []
# while True:
#     new_i = 0
#     chain = []
#     c = 0
#     f = 1
#     while f:
#         f = 0
#         for j in range(len(C[new_i])):
#             if j not in trash:
#                 if C[new_i][j] != math.inf and C[new_i][j] != 0:
#                     f = 1
#                     chain.append((new_i, j))
#                     new_i = j
#                     c += 1
#     if c == 0: break
#     mn = min(C[ch[0]][ch[1]] for ch in chain)
#     for ch in chain:
#         C[ch[0]][ch[1]] -= mn
#     sm += mn
#     for j in range(len(C)-1):
#         if all(C[j][k] in [math.inf,0] for k in range(len(C[j]))):
#             trash.append(j)
# print(sm)
# граф несвязный

# алгоритм нахождения компоненты связности графа
C = [[0,1,0,0,0,0,1],
     [1,0,1,0,0,0,0],
     [0,1,0,1,0,0,0],
     [0,0,1,0,0,0,0],
     [0,0,0,0,0,1,0],
     [0,0,0,0,1,0,0],
     [1,0,0,0,0,0,0]]
tops = {x for x in range(7)}
compons = []
temp = [0]
temp1 = []
passed = set()
while passed != tops:
    for t in temp: top = t
    for x in range(len(C[top])):
        if C[top][x] == 1:
            temp.append(x)
    passed.add(top)
    temp1 = [x for x in temp]
    while temp1:
        temp1 = [i for i in temp1 if i not in temp]
        temp += temp1
        temp1 = []
        for i in range(len(temp)):
                for x in range(len(C[temp[i]])):
                    if x not in passed and C[temp[i]][x] == 1:
                        temp1.append(x)
                        passed.add(x)
    compons.append(temp)
    for top in tops:
        if top not in temp:
            temp = [top]
            break
print(compons)





