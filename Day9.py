# coding=utf-8
# Zmodyfikuj definicję samochodu dodając mu nowy atrybut kolor.
# Kolor może być nadany przy tworzeniu samochodu, jeżeli nie domyślnym kolorem
# jest czerwony.
#Zad 3
# coding=utf-8
# Dodaj metodę przemaluj, która pozwoli na zmianę wartości atrybutu kolor.
# Metoda pozowli na przelowanie tylko jeżeli samochód jest zatrzymany.
# Jeżeli samochód jedzie zgłoś błąd.
# Utrudnienie: Wykorzystaj komendę assert

class Samochod(object):
    def __init__(self, marka, model, kolor='czerwony'):
        self.marka = marka
        self.model = model
        self.kolor = kolor
        self.jedzie = None
        self.silnik = None

    def ruszaj(self):
        self.jedzie = True
        print(f"{self.marka} ruszyl")

    def zatrzymaj(self):
        if self.jedzie == False:
            print('Samochod już stoi!')
        else:
            self.jedzie = False
            print(f"{self.marka} zatrzymal sie")

    def przemaluj(self, new_kolor):
        if self.jedzie == False:
            self.kolor = new_kolor
        else:
            print('Najpierw zatrzymaj pojazd')


auto1 = Samochod('Fiat', 'Panda')
auto2 = Samochod('Skoda', 'Fabia', 'zielona')


print(vars(auto1))
print(vars(auto2))

auto2.ruszaj()
auto2.zatrzymaj()
auto2.zatrzymaj()

auto1.przemaluj('niebieski')
auto1.zatrzymaj()
auto1.przemaluj('niebieski')
auto1.ruszaj()

