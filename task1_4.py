# вывод чисел от 0 до 10
# вывод чисел от 0 до n
# вывод четных чисел от 0 до n

# number = 0
# n = 10
# while number <= n:
#     print(number)
#     number += 1

# number = 0
# n = int(input("Введите n: "))
# while number <= n:
#     print(number)
#     number += 1

number = 0
n = int(input("Введите n: "))
while number <= n:
    if number % 2 == 0:
        print(number)
    number += 1