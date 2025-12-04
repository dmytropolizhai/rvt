"""
Riņķa līnija garums
Izveidoja: Dmytro Polizhai
"""

r = float(input("Ievadiet radiusu: "))

while r <= 0:
    print("Radiuss nevar būt negatīvais skaitlis vai 0!")
    r = float(input("Ievadiet radiusu: "))

l = 2 * 3.1415 * r
print(l)