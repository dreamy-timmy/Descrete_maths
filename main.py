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


# while weight:
#     ind = weight.index(min(weight))
#     if ribs[ind][0] in tops or ribs[ind][0] in tops: ... #sall good
#     elif ribs[ind][0] in tops and ribs[ind][0] in tops:
#         weight.remove(weight[ind])
#         ribs.remove(ribs[ind])
#     else:
#         current = [i for i in weight]
#         ind = current.index(min(current))
#         while not(ribs[ind][0] in tops or ribs[ind][0] in tops):
#             current = [weight[i] for i in range(len(weight)) if i != current.index(min(current))]
#     tops.add(ribs[ind][0])
#     tops.add(ribs[ind][1])
#     sm += weight[ind]
#     weight.remove(weight[ind])
#     ribs.remove(ribs[ind])
