# 1.3[6]. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались 
# за проезд и получали билет с номером.Счастливым билетом называют такой билет 
# с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать 
# программу, которая проверяет счастливость билета.
# Примеры/Тесты:
# 385916 >>> yes
# 123456 >>> no
# (*) Усложнение. Вывод результат на экран сделайте одной строкой(только один print), 
# для этого используйте тернарный оператор

bilet = int(input('Введите шестизначный номер билета: '))
last_number = bilet % 10
fifth_number = (bilet // 10) % 10
fourth_number = (bilet // 100) % 10
third_number = (bilet // 1000) % 10
second_number = (bilet // 10000) % 10
first_number = bilet // 100000
if first_number+second_number+third_number == fourth_number+fifth_number+last_number:
    print('YES')
else:
    print('NO')

print('YES' if first_number+second_number+third_number == 
fourth_number+fifth_number+last_number else 'NO')
