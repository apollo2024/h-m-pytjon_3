# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
#  Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
#   В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# пример
# 5
# 1 2 3 4 5
# 6
import random

size = int(input()) # вводим размер массива массива
m = []
for i in range(size):
    m.append(random.randint(1, 100)) # сделал рандомными числами чтобы проверить исправность кода
print (m)
num = int(input()) # вводим число к которуму надо найти самый близкий по величине элемент

counter = 200
counter_2 = 0
keeper = 0

for i in range(len(m)):
    counter_2 = num - m[i]
    if 0 > counter_2:
        counter_2 = -counter_2
    if counter > counter_2:
        counter = counter_2
        keeper = m[i]
        if counter == 0:
            print(f'самый близкий элемент = {keeper}')
            break
print(keeper)
