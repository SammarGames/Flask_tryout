def zijn_gelijk(getal1, getal2):
    return getal1 == getal2


test_gevallen = [
    (1, 2, False),
    (3, 3, True),
    (1, 5, False),
    (1, 1, True),
    (0, 0, True),
    (8, 8, True),
    (2, 7, False),
    (9, 9, True),
    (4, 1, False),
    (7, 7, True)
]


print("Invoer\tVerwachte uitvoer\tUitvoer\t\tOpmerkingen")
for getal1, getal2, verwacht in test_gevallen:
    resultaat = zijn_gelijk(getal1, getal2)
    opmerking = "Correct" if resultaat == verwacht else "Onjuist"
    print(f"{getal1}, {getal2}\t{verwacht}\t\t{resultaat}\t\t{opmerking}")