'================Dict(словари)====================='
# dict - изменяемыйб итерируемый неупродоченный неиндексируемый 
# тип данных для хранения данных в парах (ключ:значение)

user = {'name':'Aitma',
        'age':21, 
        'prof':'Dev'
        } 
print(user['name']) # Aitma
#ключами в словаре могут быть только не изменяемые типы данных
# если словаре есть одинаковые ключи то сохранится последний

dict1 = {'a':1, 'b':2 ,'c':3, 'a':4}
print(dict1) # {}

print(dict1['f']) # keyError 'f'

'======================Содание======================'
user = {'a':1, 'b':2}
user - dict([('a',1), ('b',2),  ('c', 3)])
user - dict(['ab',  'cd',  'ef'])

dict1 = {}
dict1['name'] = 'Aitma'
dict1['Age']  = 15
dict1['prof'] = 'artisit'
#{"name":'Aitma', "age":15}

'=================Медоты словаря================'

# get - метод который возращает значение по ключу если такого ключа нет то возращает None то детофолтное значение
user = {
    'name':'aitma',
    'age':15,
    'prof':'dev'
}
print(user.get['name']) #Aitma

# pop - удалет пару по ключу и возращает значение
num = user.pop('age') # 15
print(num)

#popitem - удаляет последниюю пару и возращает ее 
dict1 = {'a':1, 'b':2}
num = dict1.popitem() # ('b' , 2)

# update - расшеряет словарь прами из второго словаря 
dict1 = {1:'a', 2: 'b'}
dict2 = {3:'c' , 4:"d"}

dict1.update(dict2)
print(dict1)

#Fromkeys - метод для создания нового словаря, используя список ключей
dict1 = dict.fromkeys('hi', 12)
print(dict1)

dict2 = dict.fromkeys([1,2,3], 'hello')
print(dict2)

dicy1 ={1:'a' , 2:'b'}
#keys - вщзращает все ключи dict_keys([1,2])
# values  - вощзращвет все значение dict_values(['a', 'b])
# items -  влзращает все пары dict_items([(1, 'a'), (2,'b')])
print(user.keys )
print(user.values )
print(user.items)

'=====================Итерирование словарей=========================='
user = {
    'name':'aitma',
    'age':15,
    'prof':'dev'
}

a , b = (3, 5)
for key, values in user.items(): # 
    print(key, values)
