a = float(input("Ievadiet pirmu skaitli: "))
b = float(input("Ievadiet otru skaitli: "))
c = float(input("Ievadiet trešu skaitli: "))

if a > b and a > c:
    print(f"Vislielākais skaitlis ir {a}")

if b > a and b > c: 
    print(f"Vislielākais skaitlis ir {b}")

if c > a and c > b: 
    print(f"Vislielākais skaitlis ir {c}")
