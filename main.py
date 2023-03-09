#here we gonna do some main stuff

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
I = [1,2,3,4,5,6,7,8,9,10,11,12]
ribs = [[1,2], [1,5], [1,6], [2,3], [2,4], [2,5], [2,6], [3,4],
        [3,5], [4,5], [4,7], [4,8], [5,6], [5,7], [5,8], [5,9],
        [6,8], [6,9], [7,8],[7,10], [7,11], [8,9], [8,10], [8,11], [8,12],
        [9,11], [9,12], [10,11], [11,12]]
weight = [7, 9, 2, 5, 4, 8, 2, 2, 9, 3, 8, 3, 3, 5, 1, 7, 6, 1, 6, 4, 4, 2, 7, 8, 5, 6, 1, 10, 3]
tops = set()
sm = 0
s = [None for i in range(len(I))]
tops.add(I[0])
s[I[0]-1] = 0
current = []
top = 1
ind = -1
delete = []
f = 1
while ribs:
        if ind + 1 <= len(ribs)-1: ind += 1
        else:
            if current:
                mn = s[current[0] - 1]
                t = current[0]
                for j in range(len(current)):
                    if mn > s[current[j] - 1]:
                        t = current[j]
                        mn = s[current[j] - 1]
                tops.add(t)
                top = t
                current = []
                ind = 0
                delete.sort(reverse=1)
                while delete:
                    ribs.pop(delete[0])
                    weight.pop(delete[0])
                    delete.pop(0)
            else:
                for i in range(len(I)):
                    if I[i] not in tops:
                        top = I[i]
                        tops.add(top)
                        break
        if weight and top == ribs[ind][0] and f:
            if s[ribs[ind][1] - 1]:
                    s[ribs[ind][1]-1] = min(s[ribs[ind][0]-1] + weight[ind], s[ribs[ind][1]-1])
            else:
                    s[ribs[ind][1]-1] = s[ribs[ind][0]-1] + weight[ind]
            current.append(ribs[ind][1])
            delete.append(ind)
        elif weight and top == ribs[ind][1] and f:
            if s[ribs[ind][0] - 1]:
                    s[ribs[ind][0]-1] = min(s[ribs[ind][1]-1] + weight[ind], s[ribs[ind][0]-1])
            else:
                    s[ribs[ind][0]-1] = s[ribs[ind][1]-1] + weight[ind]
            current.append(ribs[ind][0])
            delete.append(ind)
print(s)

