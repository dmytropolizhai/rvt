"""
Atrod divu veselo skaitļu lielāko kopīgo dalāmo. 
Ja skaitļi nav vienādi, tad lielāko skaitli aizvieto ar abu skaitļu starpību. Ja ir vienādi, tad pirmais no tiem ir lielākais kopīgais dalāmais.
Izveidoja: Dmytro Polizhai
"""

n1 = int(input("Ievadiet 1. veselo skaitli: "))
n2 = int(input("Ievadiet 2. veselo skaitli: "))

# Eiklīda algoritms, lai aprēķinātu LKD
a = abs(n1)
b = abs(n2)

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print(a)