"""
Sešu skaitļu summa

Izveidoja: Dmytro Polizhai
"""

print("Sešu skaitļu summas aprēķināšana", end="\n\n") # Pariet nākamajā rindā

sum_ = 0

for x in range(6): # Skaitītājs no 0 līdz 6 (6 neieskaitot)
    n = int(input(f"Ievadiet {x + 1}. veselo skaitli: "))
    sum_ += n # Summas aprēķināšana

print("\nSumma ir ", sum_)