def Prims(cost, n):
    near = [float('inf') for _ in range(n)]
    t = [[float('inf') for _ in range(n-1)]for _ in range(2)]
    min = float('inf')
    for i in range(n):
        for j in range(n):
            if cost[i][j] < min:
                min = cost[i][j]
                u = i
                v = j

    t[0][0] = u
    t[1][0] = v
    near[u] = near[v] = -1
    for i in range(n):
        if near[i]!=-1:
            if cost[i][u] < cost[i][v] :
                near[i] = u
            else:
                near[i] = v
    for i in range(1,n-1):
        min = float('inf')
        for j in range(n):
                if cost[j][near[j]] < min and near[j]!=-1:
                    min = cost[j][near[j]]
                    k = j
        t[0][i] = k
        t[1][i] = near[k]
        near[k] = -1
        for j in range(n):
            if near[j] != -1 and cost[j][k] < cost[j][near[j]]:
                near[j] = k
    return t


n = int(input("Enter the number of vertices : "))
cost = [[float('inf') for _ in range(n)]for _ in range(n)]
inf = float('inf')
# print("TO exit enter edge as -2 -2: ")
# while True:
#     i, j = list(map(int, (input("Enter the edge separated by space: ").split())))
#     if i == j == -2:
#         break
#     s = int(input("Enter the cost of edge : "))
#     cost[i][j] = s
#
# print(""" Example cost adjacency matrix
#        [[inf, 3, 2, inf, inf, inf, inf, inf],
#        [3, inf, 25, inf, inf, inf, 5, inf],
#        [2, 25, inf, 12, inf, inf, inf, 10],
#        [inf, inf, 12,inf,8,inf , inf, inf],
#        [inf, inf, inf, 8,inf, 16, inf, 14],
#        [inf, inf, inf, inf, 16, inf, 20, 18],
#        [inf, 5, inf, inf, inf, 20, inf, inf],
#        [inf, inf, 10, inf, 14, 18, inf, inf]]
# """)
cost=[[inf, 3, 2, inf, inf, inf, inf, inf],
       [3, inf, 25, inf, inf, inf, 5, inf],
       [2, 25, inf, 12, inf, inf, inf, 10],
       [inf, inf, 12,inf,8,inf , inf, inf],
       [inf, inf, inf, 8,inf, 16, inf, 14],
       [inf, inf, inf, inf, 16, inf, 20, 18],
       [inf, 5, inf, inf, inf, 20, inf, inf],
       [inf, inf, 10, inf, 14, 18, inf, inf]]
l = (Prims(cost, n))
c = 0
for i in range(len(l[0])):
    c +=cost[l[0][i]][l[1][i]]
    print("Edge:", (l[0][i],l[1][i]),"Edge Cost:",cost[l[0][i]][l[1][i]])
print("Minimum cost of spaning tree :",c)
