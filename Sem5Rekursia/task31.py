# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

#     n	0	1	2	3	4	5	6	7	8	9	10
# F_{n}	0	1	1	2	3	5	8	13	21	34	55

# Input: 7
# Output: 21    в задаче индексы, 

# def fib(n):
#     if n in (0, 1):
#         return n           # первые 3 строки базовый случай
#     return fib(n - 1) + fib(n - 2)
# print (fib(7))

fib = lambda n: n if n in (0, 1) else fib(n- 1) + fib(n - 2)
print (fib(7))

# def fib(n):
#     if n == 0:
#         return 0
#     elif n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)
# lst = []
# for i in range(10):
#     lst.append(fib(i))
# print(lst) # [1, 1, 2, 3, 5, 8, 13, 21, 34]

