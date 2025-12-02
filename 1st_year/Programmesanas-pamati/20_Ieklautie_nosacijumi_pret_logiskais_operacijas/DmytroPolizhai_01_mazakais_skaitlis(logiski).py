"""
Pieprasa ievadīt trīs veselus skaitļus un salīdzina tos, izvada kurš no viņiem ir mazākais, izmantojot loģisku operatoru "and".
Izveidoja: Dmytro Polizhai
"""


a = float(input("Ievadiet pirmu skaitli: "))
b = float(input("Ievadiet otru skaitli: "))
c = float(input("Ievadiet trešu skaitli: "))

if a < b and a < c:
    print(f"Vismazākais skaitlis ir {a}")

if b < a and b < c: 
    print(f"Vismazākais skaitlis ir {b}")

if c < a and c < b: 
    print(f"Vismazākais skaitlis ir {c}")
