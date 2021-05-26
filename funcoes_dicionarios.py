Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tel ={
	30301122: "Pericles",
	33547877: "Menelau",
	33381245: "Atreu",
	36458899: "Tieste"
	}
>>> print(tel)
{30301122: 'Pericles', 33547877: 'Menelau', 33381245: 'Atreu', 36458899: 'Tieste'}
>>> len(tel)
4
>>> del(tel[36458899])
>>> print(tel)
{30301122: 'Pericles', 33547877: 'Menelau', 33381245: 'Atreu'}
>>> tel.keys()
dict_keys([30301122, 33547877, 33381245])
>>> 
>>> 
>>> 
>>> tel.values()
dict_values(['Pericles', 'Menelau', 'Atreu'])
>>> 
>>> 
>>> 
>>> 
>>> 
>>> tel[30301122]
'Pericles'
>>> 
>>> 
>>> 
>>> 
>>> tel.get(30301122)
'Pericles'
>>> 
>>> 
>>> 
>>> tel ={
	30301122: "Pericles",
	33547877: "Menelau",
	33381245: "Atreu",
	36458899: "Tieste"
	}
>>> tel
{30301122: 'Pericles', 33547877: 'Menelau', 33381245: 'Atreu', 36458899: 'Tieste'}
>>> tel.popitem()
(36458899, 'Tieste')
>>> tel
{30301122: 'Pericles', 33547877: 'Menelau', 33381245: 'Atreu'}
>>> tel.popitem()
(33381245, 'Atreu')
>>> tel
{30301122: 'Pericles', 33547877: 'Menelau'}
>>> tel.popitem()
(33547877, 'Menelau')
>>> tel
{30301122: 'Pericles'}
>>> tel.popitem()
(30301122, 'Pericles')
>>> tel
{}
>>> tel ={
	30301122: "Pericles",
	33547877: "Menelau",
	33381245: "Atreu",
	36458899: "Tieste"
	}
>>> tel
{30301122: 'Pericles', 33547877: 'Menelau', 33381245: 'Atreu', 36458899: 'Tieste'}
>>> 36458899 in tel
True
>>> 362458899 in tel
False
>>> tel2 = {99999999: "teste1", 555511: "teste2"}
>>> tel2
{99999999: 'teste1', 555511: 'teste2'}
>>> tel.upadate(tel2)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    tel.upadate(tel2)
AttributeError: 'dict' object has no attribute 'upadate'
>>> tel.update(tel2)
>>> tel
{30301122: 'Pericles', 33547877: 'Menelau', 33381245: 'Atreu', 36458899: 'Tieste', 99999999: 'teste1', 555511: 'teste2'}
>>> len(tel)
6
>>> tel = (10, 10, 10)
>>> tel
(10, 10, 10)
>>> tel[t] = "eXcript"
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    tel[t] = "eXcript"
NameError: name 't' is not defined
>>> t = (10, 10, 10)
>>> tel[t] = "eXcript"
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    tel[t] = "eXcript"
TypeError: 'tuple' object does not support item assignment
>>> t = (10, 10, 10)
>>> tel[t] = "eXcript"
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    tel[t] = "eXcript"
TypeError: 'tuple' object does not support item assignment
>>> tel ={
	30301122: "Pericles",
	33547877: "Menelau",
	33381245: "Atreu",
	36458899: "Tieste"
	}
>>> t = (10, 10, 10)
>>> tel[t] = "eXcript"
>>> tel
{30301122: 'Pericles', 33547877: 'Menelau', 33381245: 'Atreu', 36458899: 'Tieste', (10, 10, 10): 'eXcript'}
>>> 