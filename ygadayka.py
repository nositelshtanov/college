print('Необходимо задать диапазон, которому принадлежит загаданное вами число')
low_border = int(input("Укажите нижнюю границу (не меньше 0): "))
high_border = int(input("Укажите верхнюю границу (не меньше 0): "))
degree = 0 

while True:
    if (2 ** degree) < (high_border - low_border + 1):
        degree += 1
    else: 
        break

print('degree = ', degree, ' numb = ', str(2**degree), "   - служебная инфа")

numb = 2 ** degree
if (high_border - low_border) == 0:
    print('Ваше число ', high_border)
half = numb / 2
numb = numb - half

while (degree != 0) and (low_border > -1) and (high_border > -1): 
    if (high_border - low_border) == 1:
        print('ваше число больше ', low_border, ' ?')
        answer = input()
        if answer == 'да':
            print('Ваше число ', high_border)
            break
        else: 
            print('Ваше число ', low_border)
            break
    print("число больше ", numb, ' ?')
    answer = input("")
    if answer == 'да':
        numb = numb + (half / 2 )
        half = half / 2
        print("numb ", numb, 'half ', half) 
        
    else: 
        numb = numb - (half / 2)
        half = half / 2
        print("numb ", numb, 'half ', half)
    degree -= 1
    if half == 1:
        print('число больше ', numb, ' ?')
        answer = (input())
        if answer == "да":
            print('Ваше число ', numb + 1)
            break
        else: 
            print('Ваше число ', numb)
            break
        


    

        

        




