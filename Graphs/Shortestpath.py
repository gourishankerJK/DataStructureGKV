def minimumDist(dist,visited,n) :
    min = float('inf')
    for  i in range(n) :
        if (visited[i] is False and dist[i] <= min):
          min = dist[i]
          index = i
    return index

def DJ(graph,start,n):
    dist = n*[float('inf')]
    visited = n*[False]
    dist[start] = 0
    for i in range(n):
        m = minimumDist(dist,visited,n)
        visited[m] = True
        for j in range(n):
             if (not visited[j] and graph[m][j] and dist[m] != float('inf') and dist[m] + graph[m][j] < dist[j]):
                 dist[j] = dist[m] + graph[m][j]
    return dist


n = int(input("Enter the number of vertices : "))
graph =[[0 for _ in range(n)]for _ in range(n)]
graph = [[0, 10, 20, 0, 0, 0],
               [10, 0, 0, 50, 10, 0],
               [20, 0, 0, 20, 33, 0],
               [0, 50, 20, 0, 20, 2],
               [0, 10, 33, 20, 0, 1],
               [0, 0, 0, 2, 1, 0]]
# while True:
#     i, j = list(map(int, (input("Enter the edge separated by space: ").split())))
#     if i == j == -2:
#         break
#     s = int(input("Enter the cost of edge : "))
#     graph[i][j] = s

dist = DJ(graph,int(input("Enter the staring vertex: ")),n)
print("Vertex  : Distance")
for vertex,distance in enumerate(dist):
        print(chr(vertex+65) ,"    :   " ,distance)
