# coding=utf-8
# Napisz funkcję dodającą dzielącą dwa wartości podane przez użytkownika
# (obsługującą błędne wejścia).

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Nie mozna dzielic przez 0.")
        return ''  # Nie daje na koncu None


print(division(4, 2))
print(division(4, 0))