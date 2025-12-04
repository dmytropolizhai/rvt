"""
Aprēķina lietotāja ievadīto skaitļu summu
Izveidoja: Dmytro Polizhai
"""

sum_of_n = 0.0
n = float(input("Ievadiet skaitli: "))

while n != 0:
    sum_of_n += n
    n = float(input("Ievadiet skaitli: "))

print(sum_of_n)