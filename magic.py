import random

n = int(input('кол во строк и столбцов: '))
a = [[random.randint(-20,20) for j in range(n)] for i in range(n)]
local_summ_string = []
local_summ_string_numb = 0

for i in range(n):
    for j in range(n):
        print('{:4.0f}'.format(a[i][j]), end=' ')
    print()

for i in range(n):
    for j in range(n):
        local_summ_string_numb += a[i][j] 
    local_summ_string.append(local_summ_string_numb)
    local_summ_string_numb = 0

for i in range(n):
    for j in range(n):
        local_summ_string_numb += a[j][i] 
    local_summ_string.append(local_summ_string_numb)
    local_summ_string_numb = 0

local_summ_string_numb = 0

for i in range(n):
    local_summ_string_numb += a[i][i]
local_summ_string.append(local_summ_string_numb)

b = len(local_summ_string)

d = -1
local_summ_string_numb  = 0

for j in range(n-1, -1, -1):
    d += 1
    if d > n:
        break
    local_summ_string_numb += a[d][j]
local_summ_string.append(local_summ_string_numb)
print(local_summ_string, ' - служебная информация')


for i in range(b):
    if local_summ_string[i] == local_summ_string[0]:
        foo = True
    else: 
        bar = False
try:
    if bar == False:
        print('не магический твой квадрат')
except: 
    print('квадрат магический')