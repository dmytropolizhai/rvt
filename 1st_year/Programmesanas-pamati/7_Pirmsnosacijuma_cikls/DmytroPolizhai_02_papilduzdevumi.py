"""
Pirmsnosacījuma cikls, kas aprēķina lietotāja ievadīto skaitļu summu
Saskaitāmo ievade tiek pārtraukta, ja ievada nulli

Izveidoja: Dmytro Polizhai
"""

sum_ = 0

n = float(input("Ievadiet skaitli: "))

while n != 0:
    
    sum_ += n    
    print(sum_)

    n = float(input("Ievadiet skaitli: "))    