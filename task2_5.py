# t = ()                               t[0] = 2
# print(type(t))                       print(t) заменить элементы в кортеже нельзя!
# t = (1, 5, 3,)
# print(type(t))

# v = [1, 8, 9]
# print(v)
# print(type(v))

# v = tuple(v)
# print(v)
# print(type(v))

# a,b,c = v
# print(a, b, c)

t = (1, 2, 3, 5,)
# for i in t:
#     print(i) # выведет в столбик
for i in range(len(t)):
    print(t[i])   # выведет диапазон также в столбик

