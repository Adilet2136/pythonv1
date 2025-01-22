"=====================list===================="
# списки - изменяемый , индексируемый, итерируемый тип данных предназначенный для хранение любых типов данных в  определннном порядке

list1 = [ 1 , 2, 3, 2.6,[3, 4, 5], "hi", True, False, None ]
print(list1[0])
print(list[4])
print(list1[-4])
print(list1[4][2])

list2 = list('hello world')
print(list2) ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

print(list(range(1, 10)))
# range - это функция который создает последовательность
# range(start, end(не включительно), stop
 
print(list(range(0, 10, 3)))
[1,2,3,4,5,6,7,8,9]



'========================Методы списков=========================='
#append - добовляет элемент в конце списка
list3= []
list3.append(20)
print(list3)# [20]
list3.append('hi')
print(list3) 

# pop - удаляет элеиент из списка по индексу из возращает удаленный элемент,емлт индексы не указать то удалит последний элемент

list4 = ['hi', 'hello', 'katana']
list4.pop(-1)
print(list4) 

list4 = ['hi', 'hello', 'katana']
a= list4.pop(1)
print(list4)
print (a)

# remove - удаляет элемент из списка по значению
list6 = [1, 4564,45,7,8,99,0,0]
list6.remove(45)
print(list6)

list7 = [0,1,2,3,4,5,6,7,8,9,10]
count_0=list7.count(0)
print(count_0) # 3

list7 = ['hello', 'hello', 'hello']
print(list7.count('l'))

# index - возращает инндекс перевого вхождения приятного элемента

# index - возвращает индекс первого вхождения принятого элемента

list8 = ['hi', True, False, 12, 'hi', 'good', 12, 1, 4, 0, 0, 1]
print (list8.index('hi', 2, 6))                                                                                       

# insert - добавляет элемент в список по индексу

list9 = ['hi', 12, True, False, 0]
list9.insert(1, 'hello')
print(list9)

# extend - добляет элементы приятного списка в первый список изменяя его
list1 = [1,2,3]
list2 = [0,0,0]

list1.append(list2) # [1,2,3,][0,0,0,] 
list1.append(list2) # [1,2,3,0,0,0,] 

list1.extend('str') 
print(list1)

list1.extend(123) # error


# reverse - изменяет список растовляя его елементы в обратнои порядке
list10 = [1,2,3,4,5,6,7,8,]
list10.reverse()
print(list10) # [8,7,6,5,4,3,2,1,]
print(list11)# [[6,7,8]]




#sort - сортирует список состаящий из елементов одного типа данных
list12 = [23, 34,1, 4, 1, 0, 456, 3, 56, 3, -4 ]
list12.sort()
print(list12)

list13 = ['a', 'v', 'f', 'hello', 'hi','abc' 'A'] 
list13.sort()
print(list13)

list14 =[1,2,3,]
list14.clear()
print(list14)# []


str1 = 'hello'
list1= [23, 2,1 ,4 ,0]
#         0  1   2  3  4
print(len(str1)) # 5
print(len(str1)) # 5




a = 15
b = 20

a,b = 15,20


name, age, prof = ['katana', 21 , 'Dev']

meshok = ['luk' 'kartochka', 'ogurec', 'pomidor' ]
print(meshok[0])
print(meshok[1])
print(meshok[2])
print(meshok[3])

for ruka in meshok:
    print(ruka)

list15 =[True, 'hi', 10 , False, -5, 0.5[1,2,3]]
for i in list15:
    print(i)

# Итерация - процесс прохождения по элементам последовательности (итерируемого обьекта)

for i in 'hello world':
    print(i.upper()*5)


str1 = 'hello world'
print(str1.split())       

list1 = ['a', 'b', '12', 'c']
print (''.join(list1)) # a*b*12*c




list1 =[1,2,3]
list2 = [1,2,3]

print(list1 == list2)
print(list1 is list2)


str1 = 'abc'
str2 = 'abc'

print(str1 == str2) # True
print(str1 is str2) #  True
