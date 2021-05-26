Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = {1: "aaa", 2: "bbbb" , 3: "ccc"}
>>> len(x)
3
>>> x = {1:"aaa", 2:"bbb", 3:"ccc"}
>>> del(x[1])
>>> x
{2: 'bbb', 3: 'ccc'}
>>> print(x)
{2: 'bbb', 3: 'ccc'}
>>> 
>>> 'a' in 'abcdefghij"
SyntaxError: EOL while scanning string literal
>>> 'a' in 'abcdefghij'
True
>>> 'ad' in 'abcdefghij'
False
>>> 
>>> 
>>> 
>>> retornar_ligacao = {
	'perícles': 30301122,
	'Menelau': 33547877,
	'Atreu': 33381245,
	'Tiestes': 36458899,
    }
>>> 
>>> retornar_ligacao.popitem()
('Tiestes', 36458899)
>>> retornar_ligacao.popitem()
('Atreu', 33381245)
>>> retornar_ligacao.popitem()
('Menelau', 33547877)
>>> retornar_ligacao.popitem()
('perícles', 30301122)
>>> retornar_ligacao
{}
>>> retornar_ligacao = {
	'perícles': 30301122,
	'Menelau': 33547877,
	'Atreu': 33381245,
	'Tiestes': 36458899,
    }
>>> retornar_ligacao.popitem()
('Menelau', 33547877)
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
>>> 
>>> a = {"aaa":111, "bbb":222, "ccc":333}
>>> a["zzz"]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a["zzz"]
KeyError: 'zzz'
>>> 
>>> 
>>> a = {"aaa":111, "bbb":222, "ccc":333}
>>> if a["zzz"] in a:
	 print(a["zzz"])

	 
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    if a["zzz"] in a:
KeyError: 'zzz'

>>> a = {"aaa":111, "bbb":222, "ccc":333}
>>> if a["zzz"]
SyntaxError: invalid syntax
>>> if a["zzz"]:
	print(a["zzz"])

	
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    if a["zzz"]:
KeyError: 'zzz'
>>> 
>>> a = {10:"Máximo", 5:"Meio", 1:"Mínimo"}
>>> a
{10: 'Máximo', 5: 'Meio', 1: 'Mínimo'}
>>> a[10]
'Máximo'
>>> a[5]
'Meio'
>>> b = a
>>> b
{10: 'Máximo', 5: 'Meio', 1: 'Mínimo'}
>>> a[1]= "xxxx"
>>> a
{10: 'Máximo', 5: 'Meio', 1: 'xxxx'}
>>> b
{10: 'Máximo', 5: 'Meio', 1: 'xxxx'}
>>> c = a.copy()
>>> c
{10: 'Máximo', 5: 'Meio', 1: 'xxxx'}
>>> a[1] = "yyyy"
>>> a
{10: 'Máximo', 5: 'Meio', 1: 'yyyy'}
>>> b
{10: 'Máximo', 5: 'Meio', 1: 'yyyy'}
>>> c
{10: 'Máximo', 5: 'Meio', 1: 'xxxx'}
>>> 
>>> 

>>> a = {"aaa":10, "bbb":20, "ccc":30}
>>> b = {"ddd":40, "eee":50, "ddd":60}
>>> a.update(b)
>>> print(a)
{'aaa': 10, 'bbb': 20, 'ccc': 30, 'ddd': 60, 'eee': 50}
>>> 
>>> 
>>> dicionario = {"aaa": 10, "bbb": 20, "ccc":30}
>>> for e in dicionario:
    print(e)

    
aaa
bbb
ccc
>>> #Imprimindo os valores agora
>>> for e in dicionario.values():
	 print(e)

	 
10
20
30
>>> #Iterando cada elemento contendo a chave e o valor
>>> for i in dicionario:
	i, dicionario[e]

	
Traceback (most recent call last):
  File "<pyshell#83>", line 2, in <module>
    i, dicionario[e]
KeyError: 30
>>> for i in dicionario:
	print(i, dicionario[e])

	
Traceback (most recent call last):
  File "<pyshell#85>", line 2, in <module>
    print(i, dicionario[e])
KeyError: 30
>>> for i in dicionario:
	i, dicionario[e]

	
Traceback (most recent call last):
  File "<pyshell#88>", line 2, in <module>
    i, dicionario[e]
KeyError: 30
>>> 
>>> #Convertendo dicionario em lista
>>> dicionario.keys()
dict_keys(['aaa', 'bbb', 'ccc'])
>>> dicionario.values()
dict_values([10, 20, 30])
>>> dicionario.items()
dict_items([('aaa', 10), ('bbb', 20), ('ccc', 30)])
>>> #Coerção de Tipos
>>> list(dicionario)
['aaa', 'bbb', 'ccc']
>>> #Função built.in zip
>>> #retorna uma lista contendo tuplas , onde o primeiro valor,
>>> #é o da primeira lista, e o segundo valor da tupla, correspondente,
>>> #a segunda lista
>>>  d1 = ['aaa','bbb','ccc']
 
SyntaxError: unexpected indent
>>> d1 = ['aaa','bbb','ccc']
>>> d2 = ['1', '2', '3']
>>> list(zip(d1, d2))
[('aaa', '1'), ('bbb', '2'), ('ccc', '3')]
>>> dict(zip(d1, d2))
{'aaa': '1', 'bbb': '2', 'ccc': '3'}
>>> 
>>> 
>>> #Iteração de Dicionários
>>> tel = {
    30301122: "Perícles",
    33547877: "Menelau",
    33381245: "Atreu",
    36458899: "Tiestes"
}
>>> for i in tel:
	print(i)

	
30301122
33547877
33381245
36458899
>>> for i in tel.values()
SyntaxError: invalid syntax
>>> tel.values()
dict_values(['Perícles', 'Menelau', 'Atreu', 'Tiestes'])
>>> for i in tel:
	print(tel[i])

	
Perícles
Menelau
Atreu
Tiestes
>>> 
>>> 
>>> for k, v in tel.items():
	print(k, ' - ', v)

	
30301122  -  Perícles
33547877  -  Menelau
33381245  -  Atreu
36458899  -  Tiestes
>>> 