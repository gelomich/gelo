# coding=utf-8
# Zmodyfikuj definicję samochodu dodając mu nowy atrybut kolor.
# Kolor może być nadany przy tworzeniu samochodu, jeżeli nie domyślnym kolorem
# jest czerwony.

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

auto1 = Samochod('Fiat', 'Panda')
auto2 = Samochod('Skoda', 'Fabia', 'zielona')

auto2.ruszaj()
auto2.zatrzymaj()
auto2.zatrzymaj()

print(vars(auto1))
print(vars(auto2))