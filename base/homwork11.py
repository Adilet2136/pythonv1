# 1 Задание. Найти первое четное число в списке

# Дан список чисел. Напишите программу, которая с помощью цикла for находит первое четное число в списке. 
# Если такое число найдено, программа выводит его и завершает выполнение. Если в списке нет четных чисел, выведите сообщение: 
# “Четных чисел нет”. Используйте br

# list1 = [1,2,3,4,5]
# for i in list1:
#     if i % 2 == 0:
#         print (i)
#         break
# else: 
#         print("В этом списке нету четных чисел")



# Дан список чисел. Напишите программу, которая выводит только положительные числa
# из списка, используя цикл while. Пропускайте отрицательные числа, не выводя их на экран, с помощью оператора continue.

list2 = [-23, 44, -43, 88, -6786]
count = -1
while count < len(list2) - 1:
    count += 1
    if list2[count] <= 0:
        continue 
    print(list2[count])