"""
3. uzdevums

Aprēķina vidējo aritmētisku 5 skaitļiem, skaitļus ievada lietotājs.

Izveidoja: Dmytro Polizhai
"""

print("Aprēķina vidējo aritmētisku 5 skaitļiem")

sum_ = 0

for i in range(1, 6):
    number = float(input(f"Ievadiet {i}. skaitli: "))
    sum_ += number

average = sum_ / 5

print("Vidējais aritmētiskais skaitlis ir ", average)