"""
11. uzdevums

Aprēķina ciklā eksponent funkciju.

Izveidoja: Dmytro Polizhai
"""

x = float(input("Ievadiet x: "))
n = int(input("Locekļu daudzums: "))

# for k in range(n):
#     # Faktorials, izmantojot iekšejo ciklu
#     k_factorial = 1
#     for i in range(1, k + 1):
#       k_factorial *= i 

#     print(f"{k + 1}. loceklis ir {x ** k / k_factorial}")

k_factorial = 1
for k in range(n):
    # Faktorials, izmantojot iekšejo ciklu
    if k != 0:
      k_factorial *= k

    print(f"{k + 1}. loceklis ir {x ** k / k_factorial}")
