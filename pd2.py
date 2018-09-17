input = "Ala ma kota, kot ma Ale"

li = ord(input[1:2])  # zamiana litery l z slowa Ala na cyfre w standardzie ASCII

a = input[0:1] + chr(li + 6) + input[22:] + input[7:8]
w = chr(li + 11) + input[8:9] + input[1:2] + chr(li - 3)
p = chr(li + 4) + chr(li + 7) + chr(li + 13) + chr(li - 64) + " " + input[2:3]
n = chr(li + 2) + input[2:3] + chr(li - 2) + chr(li - 10) + input[2:3] + chr(li + 6) + chr(li - 8) + chr(li + 14) + chr(li - 3) + input[22:] + chr(li - 2)
b = chr(li - 10) + input[8:9] + input[7:8] + chr(li + 7) + chr(li - 7) + chr(li + 6) + chr(121)

print(a, w, p, n, b)

#print("Arek woli psy, a najbardziej boksery")

