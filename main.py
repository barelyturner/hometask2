# Exercise1
"""
# shows us The Zen of Python
import this

# opens default browser to show a comix about Python
import antigravity

# next import doesn't work
import __hello__

# instead
import __hello__
__hello__.main()

# one more Python's joke
from __future__ import braces
"""

# Exercise2
"""
from math import sqrt
a = int(input("Type a: "))
b = int(input("Type b: "))
c = int(input("Type c: "))
result = (-b + sqrt(b ** 2 - 4 * a * c)) / 2 * a
result1 = (-b - sqrt(b ** 2 - 4 * a * c)) / 2 * a
print(result)
print(result1)
"""

# Exercise3
"""
name = str(input("Enter your name: "))
print("Hello, " + name)
"""

# Exercise4
"""
exchange_rate = 40
amount = int(input("Enter amount UAH: "))
result = amount/exchange_rate
print("You will get" + result + "USD")
"""

# Exercise5
# Два способи
"""
text = "employee_first_name"
a = text.find("_")
b = text[:a]
c = text[a+1:]
d = c.find("_")
e = c[:d].title()
f = c[d+1:].title()
print(b+e+f)
"""

"""
# Порозглядав w3c, вигадав такий спосіб
text = "employee_first_name"
a = text.find("_")
b = text[:a]
c = text[a:].replace("_", " ").title().replace(" ", "")
print(b+c)
"""

# Exercise6
# Не вдалося конвертувати дні у роки, тому трохи на так витончено як хотів
# Для такої конвертації є бібліотека dateutil, яка на сумісна з останніми версіями пітона
"""
from datetime import datetime
info = "Taras Shevchenko*1814-03-09*1861-03-10"
marker1 = info.find("*")
name = info[:marker1]
dates = info[marker1:].replace("*", " ").lstrip().replace("-", "/")
marker2 = dates.find(" ")
birthdate = dates[:marker2]
deathdate = dates[marker2:].lstrip()
d1 = datetime.strptime(birthdate, '%Y/%m/%d')
d2 = datetime.strptime(deathdate, '%Y/%m/%d')
delta = d2 - d1
deltayears = delta / 365.25
converting = str(deltayears)
marker3 = converting.find(" ")
age = converting[:marker3]
print("Name: " + name)
print("Age: " + age + " years")
"""

# Exercise7
# Вигадав тільки один спосіб. Інший підгледів
# Підкажіть будь ласка, як мало бути?
"""
number = str(input())
digit1 = int(number[0])
digit2 = int(number[1])
digit3 = int(number[2])
print(digit3 + digit2 + digit1)
"""

"""
number = str(input())
result = sum(map(int, str(number)))
print(result)
"""

"""
import re
number = "555"
print(sum(int(x) for x in re.findall(r"[0-9]", number)))
"""
