# 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b.
# Разрешается использовать только операцию умножения. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16

number = 2
rank = 0

def pow_num(x, y):
    if y == 0:
        return 1
    else:
        return pow_num(x, y-1) * x 

print(pow_num(number, rank))
