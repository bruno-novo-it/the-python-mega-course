# Udemy - The Python Mega Course

https://www.udemy.com/the-python-mega-course/

This repository was made to organize all the scripts that were used in the course i made.



uma Lista --> []

Um dicionário --> {}

Uma Tupla --> ()

Para remover um elemento conhecido em uma lista, usamos list_name.remove("Nome_do_elemento")

Se vc não conhece o elemento mas sabe o íncide do mesmo, usamos list_name.pop(Índice_na_lista)

## Dictionary

Here are more operations you can do with dictionaries

Let's say we have the following dictionary:

>>> person97 = {"name":"Jack", "surname":"Smith", "age":"29"} 

Removing pair "name":"Jack"
>>> person97.pop("name") 
'Jack' 
>>> person97 
{'surname': 'Smith', 'age': '29'} 

Adding new pair "name":"Jack"
>>> person97["name"] = "Jack" 
>>> person97 
{'surname': 'Smith', 'age': '29', 'name': 'Jack'} 

Changing an existing value
>>> person97["age"] = 30 
>>> person97 
{'surname': 'Smith', 'age': 30, 'name': 'Jack'} 

Mapping two lists to a dictionary:
>>> keys = ["a", "b", "c"] 
>>> values = [1, 2, 3] 
>>> mydict = dict(zip(keys, values)) 
>>> mydict 
{'a': 1, 'b': 2, 'c': 3} 




## Tuple

There's another datatype in Python called a tuple :

mytuple = (1, 2, "Three") 

It's exactly like a list  except:

1. You use round brackets instead of square brackets to define it.

2. A tuple is not mutable which means you can't append or remove items from tuples, unlike lists. Trying to do append to a tuple would throw an error:

>>> mytuple = (1, 2, "Three") 
>>> mytuple.append("Four")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
Tuples are rarely used but if you ever want to have a sequence that you really don't want to be changed, then tuples might be a good idea to use.