# 7.1[34]: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их
# придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, 
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они 
# разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Написать функцию, которая принимает строку текста и проверяет ее ритм (по Винни-Пуху)
# Если ритм есть, функция возвращает True, иначе возвращает False

# Примеры/Тесты:
#     <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам") -> True
#     <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> True
#     <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> False
#     <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> False
#     <function_name>("Пам-парам-пурум Пум-пурум-карам") -> True
# Примечание.

# Подумайте об эффективности алгоритма. Какие структуры данных будут более эффективны по скорости.
# Алгоритм должен работать так, чтобы не делать лишних проверок. Подумайте, возможно 
# некоторые проверки не нужны.
# (*) Усложнение.

# Функция имеет параметр, который определяет, надо ли возвращать полную информацию о 
# кол-ве гласных букв в фразах. Эта информация возвращается в виде списка словарей. 
# Каждый элемент списка(словарь) соответствует фразе.

# Примеры/Тесты:
#     <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам", False) -> True
#     <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам", True) -> (True, [{'а': 4}, {'а': 4}, {'а': 4}])
#     <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> (True, [{'а': 4}, {'а': 2, 'у': 2}, {'а': 2, 'е': 1, 'о': 1}])
#     <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> (False, [{'а': 4}, {'а': 2, 'у': 3}])
#     <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> (False, [{'а': 11}, {'у': 6, 'а': 3}])
#     <function_name>("Пам-парам-пурум Пум-пурум-карам") -> (True, [{'а': 3, 'у': 2}, {'у': 3, 'а': 2}])

str = "пара-ра-рам рам-пам-папам па-ра-па-дам"

def is_rythm_exist(text):
    glasnye = ['а', 'у', 'е', 'о']
    lst = text.split()
    text_res = list()
    for item in lst:
        idx = 0
        for letter in item:
            if letter in glasnye:
                idx += 1
        text_res.append(idx)
    print(text_res)
    if len(set(text_res)) == 1:
        print('True')
    else: 
        print('False')
    
is_rythm_exist(str)


    
    