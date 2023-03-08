# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются
# в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# mol = [int(x) for x in input().split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in input().split()]
# k = set(a)
# for i in k:
#     set_1.add(i)
# b = [int(x) for x in input().split()]
# k1 = set(b)
# for i in k1:
#     set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#     print(i, end=' ')

from random import randint
n = int(input("Первый набор чисел: "))
m = int(input("Второй набор чисел: "))
lst_1 = [randint(1, 15) for i in range(n)]
lst_2 = [randint(1, 15) for i in range(m)]
print(lst_1)
print(lst_2)
set3 = set(i for i in lst_1 for j in lst_2 if i in lst_2) # это множество позволяет упорядочить от меньш к больш
lst3 = list(set3)
print(lst3)