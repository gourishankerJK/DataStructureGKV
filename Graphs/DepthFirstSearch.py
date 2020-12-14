def DFS(g,start,n):
    visited = [0 for _ in range(n)]
    def _DFS(g,visited,start,n):
        if visited[start] == 0:
            print(start)
            visited[start] = 1
            for v in range(n):
                if g[start][v] == 1 and visited[v] == 0 :
                    _DFS(g,visited,v,n)
    _DFS(g,visited,start,n)

n = int(input("Enter the number of vertices : "))
print("""# Example of adjacency matrix :
   g = [[0, 1, 0, 1, 0, 0, 0],
#      [1, 0, 1, 1, 0, 0, 0],
#      [0, 1, 0, 0, 1, 0, 0],
#      [1, 1, 0, 0, 1, 0, 0],
#      [0, 0, 1, 1, 0, 1, 1],
#      [0, 0, 0, 0, 1, 0, 0],
#      [0, 0, 0, 0, 1, 0, 0]]""")
g = []
for x in range(n):
    g.append([])
    for y in range(n):
        print("Enter the vertices for ",x,": " )
        g[x].append(int(input()))

DFS(g, int(input("Enter the staring vertice: ")), n)
