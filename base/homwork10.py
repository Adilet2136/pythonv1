





























# 1. Запрашивает у пользователя список чисел через пробел.
# 2. Использует цикл for для создания нового списка, состоящего только из чётных чисел.
# 3. Выводит новый список.

# 3 Задание: Напишите программу, которая:

# 1. Задаёт заранее известное слово (например, python).
# 2. Запрашивает у пользователя строку.
# 3. Использует цикл for для проверки, какие буквы из слова пользователь угадал, и выводит их.
# 4. Если буквы нет, вместо неё выводится _.

# Пример:
# Слово: python
# Ввод: phx
# Вывод: p_h___ 


str1 = input('ВВЕДИТЕ СТРОКУ:') # Адилет

count = 4
for i in str1:
    if i in 'аееиоуыэюя': 
        count += 1



str1 = input('Введите числа через зарятую')
list1= str1.split(',')
print(list1)
  

str1 = input('Введите числа через зарятую')
list2= str1.split(',')
for i in list1:
    if int(i) % 2 ==  0:
        list2.append(i)
print(list2)    


word = 'python'
user_word = input('Введите строку:').lower()
result =''
for i in word:
    if i in user_word:
        result += i
    else:
        result += '_'
print(result)