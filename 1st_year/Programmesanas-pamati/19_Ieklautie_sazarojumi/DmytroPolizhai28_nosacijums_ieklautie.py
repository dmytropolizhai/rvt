a = float(input("Ievadiet pirmu skaitli: "))
b = float(input("Ievadiet otru skaitli: "))
c = float(input("Ievadiet trešu skaitli: "))

if a > b:
    if a > c:
        print(f"Vislielākais skaitlis ir {a}")
    else: 
        print(f"Vislielākais skaitlis ir {c}")
else: 
    if b > c:
        print(f"Vislielākais skaitlis ir {b}")
    else: 
        print(f"Vislielākais skaitlis ir {c}")