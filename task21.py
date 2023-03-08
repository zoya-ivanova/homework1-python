# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

my_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII": "S007"}]
res = []
for item in my_dict:
    # print(item.values())
    # for val in item.values():
    #     if val not in res:
    #         res.append(val)
    
    for key in item:
        val = item[key]
        if val not in res:
            res.append(val)
print(res)


# my_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII": "S007"}]
# result = set() 
# for dct in my_dict:
#     result.add(*dct.values())   # *dct.values особый тип для вывода значений из словаря/ распаковка
# print(result)

# my_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII": "S007"}]
# result = set() 
# for dct in my_dict:
#     for key, value in dct.items():
#         result.add(value)
# print(result)