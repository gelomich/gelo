# for x in range(20):
#     if x ** 2 > 100:
#         print("Kwadrat większy niż 100")
#         #break
# else:
#     print("Brak kwadratu większege od 100")

#-----------------------------------------
#Problem 1: potrzebuję listę liczbami od 20 do 38
# 1 prosty sposób:
kwadraty = []
for x in range(20, 39):
    kwadraty.append(x)

print(kwadraty)
# 2 magiczny sposób
kwadraty = [x + 4 for x in range(20, 39)]

print(kwadraty)

#-----------------------------------------
# stwórz listę zawierającą wartości podzielne przez 5
# używając list comprehension
lista_a = [10,20,332,23,234,10,435,35,234, 20, 4938, 435]

b = [x for x in lista_a if x % 5 == 0]
print(b)

#-----------------------------------------
