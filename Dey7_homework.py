# Zaimplementuj szyfr Cezara: https://pl.wikipedia.org/wiki/Szyfr_Cezara.
# Funkcja powinna przyjmować string do zaszyfrowania oraz przesunięcie.
# Funkcja powinna również ignorować spację (nie szyfrować jej).
# UWAGA: żeby pobrać listę wszystkich znaków skorzystaj z modułu string

import string


def przesunLitere(c, p, alf):
    if c in alf:
        oldIdx = alf.index(c)  # znajdz indeks
        newIdx = (oldIdx + p) % len(alf)  # przesun indeks z dzieleniem modulo o dlugosc alfabetu (aby nie wyjsc poza zakres)
        return alf[newIdx]


def przesun(secret_message, p , alf=string.ascii_lowercase):  # zwraca wynik z małymi literami
    secret_message = secret_message.lower()
    result = ""
    for c in secret_message:
        if c in alf:
            result += przesunLitere(c, p, alf)
        else:
            result += c
    return result

def cesar_cipher(secret_message):
    return przesun(secret_message)

def main():
    secret_message = "galowie atakuja"  # "lfqtbnjfyfpzof"
    k =  5
    secret_message = przesun(secret_message, k)
    print(secret_message)

if __name__ == "__main__":
    main()


# Utrudnienie 1: Funkcja ma nie szyfrować białych znaków.
# Utrudnienie 2: Wywołując moduł homework można zaszyforwać podany
# przez konsolę tekst.