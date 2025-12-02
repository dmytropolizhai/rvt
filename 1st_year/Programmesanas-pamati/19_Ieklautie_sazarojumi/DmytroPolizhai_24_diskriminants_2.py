''' Kvadrātvienādojuma a x2 + b x + c = 0 sakņu rēķināsana:
D = b2 - 4 a c, ja D > 0, tad 2 saknes,
D = 0, tad viena sakne,
D < 0, tad nav sakņu.

Izveidoja: Dmytro Polizhai

'''
from math import sqrt # kvadrātsaknes funkcijas importēšana
print("Kvadrātvienādojuma a x2 + b x + c = 0 sakņu rēķināsana\n")

a = float(input("Ievadiet a: "))
b = float(input("Ievadiet b: "))
c = float(input("Ievadiet c: "))

# Diskriminanta rēķināšana
D = b**2 - (4 * a * c)

if D >= 0: # Vai diskriminants ir lielāks vai vienāds ar 0
    if D > 0: # Vai diskriminants nav vienāds ar 0, tad aprēķinam 2 saknes
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)

        print("Dikriminants ir pozitīvs, tad\n", "x1: ", x1, "\n", "x2: ", x2)
    else: # Ja diskriminants ir nulle, tad aprēķinam vienu sakni
        x = -b / (2*a)
        print("Dikriminants ir nulle, tad x: ", x)


else: 
    print("Diskriminants ir mazāks par 0, tad nav sakņu")