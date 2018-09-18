# sprawdz czy podana liczba jest podzielna przez 3, 5 lub 7
liczba = input("Podaj liczbe ")

if liczba.isnumeric():
    liczba = int(liczba)
else:
    print("Bledna wartosc")
    exit()

if liczba % 3 == 0 or liczba % 5 == 0 or liczba % 7:
    print("Liczba jest podzielna przez 3, 5 lub 7")
else:
    print("Liczba nie jest podzielna przez 3, 5 ani 7")