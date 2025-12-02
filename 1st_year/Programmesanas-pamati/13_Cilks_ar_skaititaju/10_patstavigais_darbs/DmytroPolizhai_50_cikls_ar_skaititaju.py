"""
Parāda šādu vērtību tabulu, veselo skaitļu no 9 līdz 3 (3 neieskaitot, bet ieskaitot 4) kvadrātsaknes

Izveidoja: Dmytro Polizhai
"""
from math import sqrt

print("-"*39)
print(" Skaitlis  | Kvadrātsaknes no skaitli |")
print("-"*39)

for n in range(9, 3, -1):
    print(f"  {n}        | {sqrt(n)}")

print("-"*39)