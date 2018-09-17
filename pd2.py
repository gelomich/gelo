int = "Ala ma kota, kot ma Ale"

l = ord(int[1:2])

a = int[0:1] + chr(l + 6) + int[22:] + int[7:8]
w = chr(l + 11) + int[8:9] + int[1:2] + chr(l - 3)
p = chr(l + 4) + chr(l + 7) + chr(l + 13) + chr(l - 64) + " " + int[2:3]
n = chr(l + 2) + int[2:3] + chr(l - 2) + chr(l - 10) + int[2:3] + chr(l + 6) + chr(l - 8) + chr(l + 14) + chr(l - 3) + int[22:] + chr(l - 2)
b = chr(l - 10) + int[8:9] + int[7:8] + chr(l + 7) + chr(l - 7) + chr(l + 6) + chr(121)

print(a, w, p, n, b)

#print("Arek woli psy, a najbardziej boksery")

