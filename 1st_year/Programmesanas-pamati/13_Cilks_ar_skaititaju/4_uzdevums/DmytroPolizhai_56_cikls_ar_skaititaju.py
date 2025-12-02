"""
4. uzdevums

Ciklu lietošana līkņu veidošanā, izskaitļo funkcijas y = x^2 vērtības, ja x mainās diapazona no -3 līdz 3 ar soli 0,5.

Cikls atkārtosies: 13 reizes

Izveidoja: Dmytro Polizhai
"""

x = -3

for i in range(1, 14):
    print(f"{i}. y = x^2 = {x}^2 = {x**2}")
    x += 0.5