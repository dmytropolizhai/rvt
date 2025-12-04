"""
Velk kvadrātsakni no lietotāja ievadītajiem skaitļiem. Programma darbu beidz, kad tiek ievadīts negatīvs skaitlis
Izveidoja: Dmytro Polizhai
"""

n = float(input("Ievadiet skaitli: "))

while n != 0:
    print(f"Skaitlis kvadrātā ir {n ** (1/2)}")
    n = float(input("Ievadiet skaitli: "))
    