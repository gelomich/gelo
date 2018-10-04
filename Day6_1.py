# wczytaj 3 pierwsze linijki pliku tekst1.txt wykorzystujac komede with

path = 'tekst1.txt'
with open(path, 'r') as plik:
    for ii in range(3):
        print(plik.readline())
