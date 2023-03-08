# Задача №33. Решение в группах Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
# решение не рекурсия

# lst = [int(input("Введите отметку: ")) for _ in range(5)]
# x = min(lst)
# y = max(lst)
# lst2 = [x if i == y else i for i in lst]
# print(lst2)

import random
n = int(input("Введите количество отметок: "))
arr = [random.randint(0, 10) for _ in range(n)]
print(arr)

for i in range(len(arr)):
    if arr[i] == max(arr):
        arr[i] = min(arr)
print(arr)
