## Zadanie 1
# coding=utf-8
# Napisz funkcję dodającą dzielącą dwa wartości podane przez użytkownika
# (obsługującą błędne wejścia).

# def division(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         print("Nie mozna dzielic przez 0.")
#
#     except Exception:
#         print("Podane wejscie jest bledne")
#     return ''  # Nie daje na koncu None
#
#
# print(division(4, 2))
# print(division(4, 0))
# print(division(None, 0))

## Zadanie 2

# Zmodyfikuj kod tak aby korzystał z instrukcji try-except.
# w celu zarówno obsługi błędów jak i zapewnienia zamknięcia strumienia do pliku
# (usunąć instrukcję with)

import os

# file_path = "dane.txt"
#
# try:
#     file = open(file_path)
#     #print("Sciezka istnieje, otwieram plik")
#     #print(file.read())
#
# except FileExistsError:
#     print("Sciezka nie istnieje!")
#
# else:
#     file.close()

# if os.path.exists(file_path):
#     print("Sciezka istnieje, otwieram plik")
#     with open(file_path, 'r') as file:
#         print(file.read())
# else:
#     print("Sciezka nie istnieje!")

## Zadanie 3

# coding=utf-8
# Zmodyfikuj funckję calculator tak by w jej implementacji wykorzystać słownik
# oraz bibiliotekę operator (dla działań dodawania odejmowania itd.
# Obsługę podania błędnego wejścia zrealizuj przez intrukcję try-except.

from operator import add, sub, mul, truediv

calc_func = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": truediv,
}

def calc(func, arg1, arg2=1):
    try:
        return calc_func[func](arg1, arg2)
    except KeyError:
        return ("Podano błędne dane")
    except TypeError:
        return ("Podane argumenty maja bledny typ")

print(calc('+', 2, 2))
print(calc('-', 2, 2))
print(calc('*', 6, 2.5))
print(calc('/', 2, 2))
print(calc('/', 4))
print(calc('&', 4))
print(calc('+', 4, [9]))

