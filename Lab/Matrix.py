row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
matrix = [[int(input("Enter the  element: ")) for i in range(col)] for j in range(row)]
for r in matrix :
    print(r)
minimum = matrix[0][0]
maximum = matrix[0][0]
for i in range(row):
    for j in range(col):
        if minimum > matrix[i][j]:
            minimum = matrix[i][j]
        elif maximum < matrix[i][j]:
            maximum = matrix[i][j]
print("Maximum number is :",maximum,"and minimum number is :",minimum)
