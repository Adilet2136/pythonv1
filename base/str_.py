"==========================Сроки (str) ========================"
# строки - неизменяемы тип данных каторый предназначен для хранения текста (последовательности символов), 
#  заключенного в одинарные или двойные кавычки

string1 = "строка с одинарноми кавычками"

string2 ="строка с двойными кавычками"

# error = "не правильная строка"

string3 = "Don't" 

string4 = "Мой никнейм 'Aitma' "

string5 = '''Привет 
как 
дела '''

string6 = """Привет 
как 
дела 
"""

str7 = 'Привет' + "" + 'Как дела?'
print (str7) 

# Конткатенация- это склеивоние строк 

# str8 ='Ha ' * 100
# print(str8)

'=====================================Экрагизация=============================='
# '\n' - перенос строки на новую строку 
print('Hello world') # hello world 
print('hello\nworld') # hello
                      # world
        
# '\t' - табуляция 
print('hello\tworld') # hello   world 

print('Don\'t')
print("Don\"t")



# '\v' - перенос на новую строку смещением вправо на длину предыдущеи строки

print('hello\vworld\vmetalbs')

# '\r' - перенос каретки на начало строки
print('hello\rGo')


'==============================Фарматирование строк============================'
title ='ipone 16'
price = 150000
message = f'Я купил {title} за {price} сом '
print(message)

message2 = 'я купил {} за {} сом '
print(message2.formant(title,price))
print(message2.format('Samsung Z Flip', 12000))

message3 = 'Я купил %s за %s сом' 
print(message3 % (title, price)) 
   

'===================================Методы строк==============================='
# методы - функций , которые относятся к опреденному классу (типу данных) , к ним мы обращаемся через точку

str = 'hello'
print(str1.upper()) # hello -> HELLO
print('HELLO'.lower()) # HELLO ->hello
print('HeLlo'.swapcase()) # HeLlo _> helLo
priint('hello world'.capitalize()) # hello world -> Hello world
print('helLo woRld'.title()) # helLO woRld -> Hello World 

print(dir(str))


print('hello.center(11)') # '    hello    '
print('hello'.center(11, '*')) # " *******hello*********"
print('hello world'.count('l'))# 3
print('hello world'.count('ll'))# 3
print('hello world'.startswith('he')) # True 
print('hello world'.startswith('H')) # False 
print('hello world'.endswith('rld')) # True
print('hello world'.endswith('gsd')) # false
print('hello world'.islower()) # True  
print('heLlo world'.islower()) # false
print('hello world'.isupper()) # false
print('hello world'.isupper()) # false  
print('HELLO WORLD'.isupper()) # True 
print('hello'.isdigit()) # false
print('43434'.isdigit()) # True
print('hello'.isalpha()) # True
print('1242'.isalpha()) # false
print('hello 123'.isalnum()) # false
print('hello123'.isalnum()) # true
print('hello'.isalnum()) # true
print('123'.isalnum()) # true
print('hello world'.replace('e','i')) # hillo world
print('hello world'.replace('e','i'))  # helli wirld 
print('hello world'.replace('e','i',1)) # heiio worid
''.split()
''.join()

'========================Индексы======================='
# штвух- порядковый номер элемента в последовательности (символа в строке) индексация начинается с 0
# ' h e l l o   w o r l d
# 0 1 2 3 4 5 6 7 8 9 10

string = 'hello world'
print(string[0]) # h  
print(string[10]) # d
print(string[-1]) # d
print(string[5]) # ' '
print(string[2:5]) # llo
print(string[0:4]) # hell
print(string[4:]) # o world
print(string[:]) # hello world
print(string[::2]) # hlowrd
print(string[::-1]) # dlrow olleh
print(string[-5:-1]) # worl

str10 = "hello"
print(str10.replace('h', 'd')) # dello
print(str10)
# срез - подмтрока строки (часть строки ) -  str[start:end:step]
print(string[2:5]) # 

