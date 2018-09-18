# sprawdz czy podana liczba jest podzielna przez 3, 5 lub 7
liczba = input("Podaj liczbe ")

# sprawdzenie czy liczba to napewno liczba
if liczba.isnumeric():
    liczba = int(liczba)    # rzutowanie
else:
    print("Bledna wartosc")
    exit()

# wlasciwy kod
# liczba podzielna przez ... jak reszta rowna 0 to jest podzielna ( == 0 )
if liczba % 3 == 0 or liczba % 5 == 0 or liczba % 7:
    print("Liczba jest podzielna przez 3, 5 lub 7")
else:
    print("Liczba nie jest podzielna przez 3, 5 ani 7")