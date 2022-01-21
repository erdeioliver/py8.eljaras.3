'''
3. Feladat
Írj eljárást, amely paraméterül kapott 2 számot összehasonlít, és a képernyőre kiírja, melyik a nagyobb szám! Kezeld azt az esetet is, ha a két szám egyenlő!
'''

def elemzo(x, y):
    if x < y:
        return print(f"A nagyobb számunk: {y}")
    elif y < x:
        return print(f"A nagyobb számunk: {x}")
    else:
        return print(f"A két számunk egyenlő {x}")

szam1 = int(input("Kérnék egy számot! "))
szam2 = int(input("Kérnék egy másik számot! "))

elemzo(szam1, szam2)