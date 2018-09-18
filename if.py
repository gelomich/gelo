# Zadanie 1
#
#name = input("podaj imie: ")
#
#if name[-1] == "a"  or name[-1] == "A":
#    print("Witaj kolezanko")
#else:
#    print("Witaj kolego")

# Zadanie 2
#
temp = input("Jaka jest temperatura na klimatyzatorze? ")

if temp.isnumeric():
    temp = float(temp)      # rzutowanie
else:
    print("Wpsiales bledna wartosc")
    exit()

ideal_temp = 24.0

if temp < ideal_temp:
    print("Jest za zimno")
elif temp > ideal_temp:
    print("Jest za cieplo")
else:
    print("Jest ok")