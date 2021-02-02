import random

low_border = int(input("Укажите нижнюю границу: "))
high_border = int(input("Укажите верхнюю границу: "))

number = random.randint(low_border, high_border)

print('Компьютер загадал число в вашем диапазоне. Попробуйте отгадать')

while True:
    answer = int(input('Ваше число: '))
    if answer == number:
        print('Угадано. число - ', answer)
        break
    else: 
        print('Не угадано.')
        if answer < number: 
            print('Число больше')
        else: 
            print('Число меньше')
