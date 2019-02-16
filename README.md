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



# OPEN and READ FILES

Depois de usar um myfile.read(), todo o arquivo vai ser lido e/ou armazenado em alguma variável. se o mesmo comando for executado, sem utilizar o myfile.close(), o resultado será um vazio, pois todo o arquivo ja terá sido lido e o cursor vai estar no final do arquivo. É necessário fechar(close()) e refazer o processo.


# DATE and TIME

Code	Meaning	Example
%a	Weekday as locale’s abbreviated name.	Mon
%A	Weekday as locale’s full name.	Monday
%w	Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.	1
%d	Day of the month as a zero-padded decimal number.	30
%-d	Day of the month as a decimal number. (Platform specific)	30
%b	Month as locale’s abbreviated name.	Sep
%B	Month as locale’s full name.	September
%m	Month as a zero-padded decimal number.	09
%-m	Month as a decimal number. (Platform specific)	9
%y	Year without century as a zero-padded decimal number.	13
%Y	Year with century as a decimal number.	2013
%H	Hour (24-hour clock) as a zero-padded decimal number.	07
%-H	Hour (24-hour clock) as a decimal number. (Platform specific)	7
%I	Hour (12-hour clock) as a zero-padded decimal number.	07
%-I	Hour (12-hour clock) as a decimal number. (Platform specific)	7
%p	Locale’s equivalent of either AM or PM.	AM
%M	Minute as a zero-padded decimal number.	06
%-M	Minute as a decimal number. (Platform specific)	6
%S	Second as a zero-padded decimal number.	05
%-S	Second as a decimal number. (Platform specific)	5
%f	Microsecond as a decimal number, zero-padded on the left.	000000
%z	UTC offset in the form +HHMM or -HHMM (empty string if the the object is naive).	
%Z	Time zone name (empty string if the object is naive).	
%j	Day of the year as a zero-padded decimal number.	273
%-j	Day of the year as a decimal number. (Platform specific)	273
%U	

Week number of the year (Sunday as the first day of the week) as a zero padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.	39
%W	

Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0.	39
%c	Locale’s appropriate date and time representation.	Mon Sep 30 07:06:05 2013
%x	Locale’s appropriate date representation.	09/30/13
%X	Locale’s appropriate time representation.	07:06:05
%%	A literal '%' character.	%


Note: Examples are based on datetime.datetime(2013, 9, 30, 7, 6, 5)

Source: http://strftime.org/

