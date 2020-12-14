def union(sets,u,v):
    if sets[u] < sets[v]:
        sets[u]+=sets[v]
        sets[v] = u
    else :
        sets[v]+=sets[u]
        sets[u] =v
    return sets
def find(sets,u):
    x= u
    v=0
    while sets[x]>0:
        x = sets[x]
    while u!=x:
        v = sets[u]
        sets[u] = x
        u =v
    return x
def kruskal(cost,n):

    t = [[float('inf') for _ in range(n-1)]for _ in range(2)]
    sets = [-1 for _ in range(n)]
    edges =[[]for j in range(3)]
    for i in range(n):
        for j in range(i,n):
            if cost[i][j] != float('inf'):
                edges[0].append(i)
                edges[1].append(j)
                edges[2].append(cost[i][j])
    i=0
    included = [0 for _ in range(len(edges[0]))]
    while i<n-1:
        min = float('inf')
        for j in range(len(edges[0])):
            if included[j] == 0 and edges[2][j] < min :
                min = edges[2][j]
                u = edges[0][j]
                v = edges[1][j]
                k = j
        if find(sets,u) != find(sets,v):
            t[0][i]= u
            t[1][i]= v
            union(sets,find(sets,u),find(sets,v))
            i+=1
        included[k]=1
    return t
n = int(input("Enter the number of vertices : "))
cost = [[float('inf') for _ in range(n)]for _ in range(n)]
inf = float('inf')
print("TO exit enter edge as -2 -2: ")
print("""example :
       [[inf, 3, 2, inf, inf, inf, inf, inf],
       [3, inf, 25, inf, inf, inf, 5, inf],
       [2, 25, inf, 12, inf, inf, inf, 10],
       [inf, inf, 12,inf,8,inf , inf, inf],
       [inf, inf, inf, 8,inf, 16, inf, 14],
       [inf, inf, inf, inf, 16, inf, 20, 18],
       [inf, 5, inf, inf, inf, 20, inf, inf],
       [inf, inf, 10, inf, 14, 18, inf, inf]]""")
# while True:
#     i, j = list(map(int, (input("Enter the edge separated by space: ").split())))
#     if i == j == -2:
#         break
#     s = int(input("Enter the cost of edge : "))
#     cost[i][j] = s
cost =[[inf, 3, 2, inf, inf, inf, inf, inf],
[3, inf, 25, inf, inf, inf, 5, inf],
[2, 25, inf, 12, inf, inf, inf, 10],
[inf, inf, 12,inf,8,inf , inf, inf],
[inf, inf, inf, 8,inf, 16, inf, 14],
[inf, inf, inf, inf, 16, inf, 20, 18],
[inf, 5, inf, inf, inf, 20, inf, inf],
[inf, inf, 10, inf, 14, 18, inf, inf]]
l= kruskal(cost,n)
c = 0
for i in range(len(l[0])):
    c +=cost[l[0][i]][l[1][i]]
    print("Edge:", (chr(l[0][i]+65),chr(l[1][i]+65)),"Edge Cost:",cost[l[0][i]][l[1][i]])
print("Minimum cost of spaning tree :",c)
