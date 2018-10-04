# Wypisz które liczby z tupli "b" występuję w liście "liczby"


liczby = [2, 4324, 25, 43, 4, 5765, 756, 7, 3425, 325, 364]
b = (1, 2, 3, 4, 5, 6, 7, 8, 9)

for x in b:
    if x in liczby:
        print(x)

# Napisz funkcję wyświetlającą imię i nazwisko, imie z duzej litery, a nazwisko wielkimi literami


def name(first_name, last_name):
    print(first_name.capitalize(), ' ', last_name.upper())

name('maciej', 'kwiatkowski')
cos = input()
# print(cos)



# Napisz funkcję podnoszącą podaną wartość (number) do podanej potęgi (index)
# Jeżeli potęga nie jest podana, podnieś do 2. potęgi


def my_pow(number, index=2):
    return number ** index

print(my_pow(4, 3))
print(my_pow(2))


