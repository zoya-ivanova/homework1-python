# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10  сумма= (Петя+Сережа)+2(Петя+Сережа)=х+х+2(х+х)=6х

sum = int(input("Введите число журавликов: " ))
print("Петя и Сережа сделали по", sum // 6, "журавлика(ов) каждый, а Катя сделала", (sum // 6)*4,"журавлика(ов)")
