a = int(input("Введите число:"))
fib1 = 0
fib2 = 1
fibonacci = 1
n = 1

while fibonacci < a:
    fibonacci = fib1 + fib2
    fib1 = fibonacci
    n += 1
print(n)

