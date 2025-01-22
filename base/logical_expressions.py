'========================Логические и условные операторы======================'
# логические операторы - выражения , которые возращаются  True , если выражение , flase - если выражение не верное 

"Равенство"
10 == 5 # false
5 == 5 # True
# print('hi' == 2)    
"hi == hi"
 

"не равенство"
4 != 5 # True
5 != 5 # Falseb

'Больше'
10 > 10 # False
4 > 1 # true 

'Меньше'
5 < 4 # False 
10 < 10 # false



'БОльше ил равно'
10 >= 4 # true false
10 >= 10 # True
4 >= 5 # False 

'Меньше или равно'
10 <= 10 # true 
5 <= 10 # true 
10 <= 5# false 


'====================And Or Not=================='
# and - и
#or - или
# not - нет
a = 5
b = 6

# true  # true
a == 5 and b ==6

#false  и  true
a == 7 and b ==6 #false

# false      #true
a > 10 and b <= 6  # false 

#false        #false 
a == 0 and b == 0 # false

# если все части выражение true это бутед true
# если хотя бы одна часть выражения False  будет false

#TRue     # true 
a == 5 or b == 6 # true 

#false  или true 
a > 10 or b == 6    

a < 20  or b == 10 # true

#false или False 
a == 1 or b == 1 # false 

# если хотя бы одна часть выражения возращает true - будет True


# not True -> false 
# not False -> # true

    # true   
not a == 5  # false

#true                 # True
not a < 20 or not b == 6 # false
# true            false    true      true          false      false 
not b > 20 and a == 5 or b == 6 or a <= 6 or not a == 5 and 5 == 10

#true

'==========================Булевый тип============================'
# булевый тип данных имееи всего 2 значения True и False

bool(1) # true 
bool(-12) # true
bool(0) # False

bool('hello') # true 
bool(' ') # true
bool('_') # true
bool('') # false

bool(true) # true
bool(false) # false

'=======================NoneType========================'
# none неизменяемый тип данных с одним значением none который используется для обозночения отсутсвия значения

a = None
bool(None) # false     

a = 5
b = 5

a == b # true
print(a is b) 
  
a="hi"  
b="hi"
print(id(a), id(b))


'=========================Условные операторы========================='
# условные операторы - конструкцияб которая используется для того чтобы при разных данных код роатал по разнаму в зависимости от условия

if 'условие1':
    'действиу1'

pogogda = input("Введите погоду: ")
if pogogda == "солнечно":
    print("Взять солнц-очки")
elif pogogda == "дождливо":
    print("Взять зонтик")
else:
    print("ПОка")






'=========================Тернаный оператор==========================='
# тернаный оператор - условие в одну строк   

num =23
if num > 0: # условие1 
    chislo = 'положительное' # действие1
else:
    chislo = 'отрецательное' # действие2    

# chislo = действие1 if условие1 else действие2

chislo = 'положительное' if num > 0 else 'отрицательное'
print(chislo)