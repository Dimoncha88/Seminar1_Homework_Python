# 2.1[10]: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно 
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть. 
# Количество монет и их положение (0 или 1) пользователь вводит с клавиатуры.
# Примеры/Тесты:
# Введите кол-во монет>? 5
# Положение монеты 0: 0 или 1>? 1
# ...
# 1 0 1 1 0
# Кол-во монет, чтобы перевернуть: 2

n = int(input('Введите количество монет: '))
count = 0
coin_orel = 0
coin_reshka = 0
while count < n:
    coin = int(input('Положение монеты орел "0" или решка "1": '))
    if coin == 0:
        coin_orel +=1
    else:
        coin_reshka +=1
    count +=1
print(f'Кол-во монет, чтобы перевернуть: {coin_orel}' if coin_orel <= coin_reshka 
        else f'Кол-во монет, чтобы перевернуть: {coin_reshka}')
