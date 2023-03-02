# colors = {'red', 'green', 'blue'}
# print(colors)
# colors.add('red')
# print(colors)
# colors.add('grey')
# print(colors)
# colors.remove('red') # {'green', 'grey', 'blue'}  
# print(colors)
# colors.remove('red') # ошибка
# colors.discard('red')
# print(colors)  # {'green', 'grey', 'blue'}  
# colors.clear()
# print(colors) # set()

# a = {1, 2, 3, 4, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()    {1, 2, 3, 4, 5, 8}
# print(c)
# u = a.union(b)  {1, 2, 3, 4, 5, 8, 13, 21}
# i = a.intersection(b)   {8, 2, 5}
#dl = a.difference(b) # {1, 3, 4}
#print(dl)
#dr = b.difference(a)  # {13, 21}
# print(dr)
# q = a.union(b).difference(a.intersection(b))  # {1, 3, 4, 13, 21}
# print(q)

# a = {1, 8, 6}
# b = frozenset(a)
# print(b)

# list_1 = []  # 1-вариант
# for i in range(1, 10):
#     list_1.append(i)
# print(list_1)

list_1 = [i for i in range(1, 10)] # второй вариант
print(list_1)
list_1 = [i for i in range(1, 10) if i % 2 == 0] 
print(list_1)
list_1 = [i * 2 for i in range(10) if i % 2 == 0] 
print(list_1)





