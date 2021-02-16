import random

n = int(input('кол во строк и столбцов: '))
a = [[random.randint(-20,20) for j in range(n)] for i in range(n)]
matrix = []
temp_matrix = []


for i in range(n):
    for j in range(n):
        print('{:4.0f}'.format(a[i][j]), end=' ')
    print()

print(a)

for i in range(n):
    for j in range(n-1, -1, -1):
        matrix.append(a[j][i])
print(matrix)





