import datetime

birthyear = input("Podaj rok urodzenia ")
rok_obecny = int(datetime.datetime.now().year)

birthyear = int(birthyear)
age = str(rok_obecny - birthyear)
print("Masz" + " " + age + " " + "lat")

