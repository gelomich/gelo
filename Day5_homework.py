# Napisz funkcję (z docstringiem) calc, która będzie wykonywała podstawowe
# działania arytmetyczne (dodawanie, odejmowanie, mnożenie, dzielenie).
# Funkcja powinna przyjmować 3 argumetny:
# działanie (jako string), argument 1, argument 2 (domyślnie o wartości 1).
# Wywołaj funkcję na podanej liście parametrów

"""Działania"""
# +
def add(num1, num2):
    return num1 + num2
# -
def subtract(num1, num2):
    return num1 - num2
# *
def multiply(num1, num2):
    return num1 * num2
# /
def divide(num1, num2):
    return num1 / num2

def calc():
    """Kalkulator"""
    operator = str(input('''   Podaj działanie: 
    '''))
    arg1 = int(input('''   Podaj pierwszą cyfre: 
    '''))
    arg2 = int(input('''   Podaj drugą cyfrę: 
    '''))


    if operator == '+':
        print(arg1, "+", arg2, "=", add(arg1, arg2))

    elif operator == '-':
        print(arg1, "-", arg2, "=", subtract(arg1, arg2))

    elif operator == '*':
        print(arg1, "*", arg2, "=", multiply(arg1, arg2))

    elif operator == '/':
        print(arg1, "/", arg2, "=", divide(arg1, arg2))

    else:
        print('Nie podałeś działania.')

    again()

"""Powtórzenie"""
def again():
    calc_again = input('''
Jeszcze raz?
Jeśli TAK naciśni T, a jeśli nie naciśnij N.
''')

    if calc_again.upper() == 'T':
        calc()
    elif calc_again.upper() == 'N':
        print('Zapraszam ponownie.')
    else:
        again()

calc()

# test_parameters = [

#     ('+', 2, 2),
#     ('-', 5, 7),
#     ('*', 6, 2.5),
#     ('/', 4),
# ]


# Utrudnienie 1: Poproś o podanie parametrów przez konsolę
# Utrudnienie 2: Wykorzystaj podaną funkcję w programie kalkulator,
# która najpierw zapyta o działanie (arytmetyczne lub przerwanie programu),
# a póżniej o argumenty działania
