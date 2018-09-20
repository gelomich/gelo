rok = input("Podaj rok ")
# rzutowanie
rok = int(rok)

message_true = "Rok przestepny"
message_false = "Rok nie jest przestepny"

if rok % 4 == 0 and rok % 100 != 0:
    print(message_true)
elif rok % 400 == 0:    # to samo co na gorze
    print(message_true)
else:
    print(message_false)