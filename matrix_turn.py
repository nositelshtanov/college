import random

n = int(input('кол во строк и столбцов: '))
a = [[random.randint(-20,20) for j in range(n)] for i in range(n)]
start = 0
end = n
matrix = []
temp = []
rezult_matrix = []


for i in range(n):
    for j in range(n):
        print('{:4.0f}'.format(a[i][j]), end=' ')
    print()

for i in range(n):
    for j in range(n-1, -1, -1):
        matrix.append(a[j][i])

for i in range(n):
    temp = matrix[start:end]
    rezult_matrix.append(temp)
    temp = []
    start += n 
    end += n

print()

for i in range(n):
    for j in range(n):
        print('{:4.0f}'.format(rezult_matrix[i][j]), end=' ')
    print()




