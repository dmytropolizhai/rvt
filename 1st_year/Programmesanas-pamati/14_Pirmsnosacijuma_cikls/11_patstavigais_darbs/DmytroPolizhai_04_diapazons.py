"""
Aprēķina vērtību  y = x2 - 3 , ja x mainās diapazona no -3.5 līdz 2 ar soli 0,5.
Izveidoja: Dmytro Polizhai
"""
x = -3.5

while x <= 2:
    y = x ** 2 - 3
    print(x, "=>", y)

    x += 0.5