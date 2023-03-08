# Задача №27. Общее обсуждение
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов или символами конца строки.Определите,
# сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore;The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore,I'm sure that the shells are sea
# shore shells.
# Output: 19
# 1 вариант решения
# print(len(set("She sells sea shells on the sea shore;The shells that she sells are sea shells I'm sure." 
#     "So if she sells sea shells on the sea shore,I'm sure that the shells are sea shore shells".lower().split())))
# 2 вариант
text = "She sells sea shells on the sea shore;The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore,I'm sure that the shells are sea shore shells"
text1 = " "
for item in text:
    if item.isalpha() or item == " ": # проверяет полностью ли состоит из букв
        text1 += item
print(text1)
print(len(set(text1.lower().split())))