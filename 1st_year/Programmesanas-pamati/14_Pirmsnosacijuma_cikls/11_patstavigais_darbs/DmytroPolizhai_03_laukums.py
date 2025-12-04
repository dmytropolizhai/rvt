"""
Aprēķina riņķa laukuma vērtību. Rādiusu vērtības ievada lietotājs. Programma darbu beidz, kad ievadīts negatīvs skaitlis vai nulle.
Izveidoja: Dmytro Polizhai
"""
from math import pi

r = float(input("Ievadiet radiusu: "))

while r > 0:
    S = pi * r**2 
    print(S)
    r = float(input("Ievadiet radiusu: "))
