# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# пример
# 5
# 1 2 3 4 5
# 3
# -> 1
import random


size = int(input())
list = [random.randint(0, 50) for i in range(size)]
print(list)
print(f"число которое надо найти")
find_out = int(input())
counter  = 0 
for i in list:
    if find_out == i:
        counter += 1
print(f'найдено совпадений = {counter}')