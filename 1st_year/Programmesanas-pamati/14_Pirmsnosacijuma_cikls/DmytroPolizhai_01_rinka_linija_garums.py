"""
Riņķa līnija garums
Izveidoja: Dmytro Polizhai
"""

from math import pi

r = float(input("Ievadiet radiusu: "))

while r <= 0:
    print("Radiuss nevar būt negatīvais skaitlis vai 0!")
    r = float(input("Ievadiet radiusu: "))

l = 2 * pi * r
print(l)