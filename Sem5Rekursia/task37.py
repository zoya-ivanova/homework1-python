# Задача №37. Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# def revers(n, s = " "):
#     if n > 0:
#         return revers (n-1, input() + s)
#     return s
# print(revers(5))

# def revers(n):
#     if n == 0:
#         return " "
#     val = input()
#     return revers(n-1) + f"{val}"
# print(revers(5))

from random import randrange

def func(n):
    if n == 0:
        return '->'
    var = randrange(n)
    print(var, end=" ")
    return f"{func(n - 1)} {var}"
print(func(8))
