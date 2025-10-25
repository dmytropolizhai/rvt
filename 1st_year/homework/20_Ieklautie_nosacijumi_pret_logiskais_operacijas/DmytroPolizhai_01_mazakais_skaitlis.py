a = float(input("Ievadiet pirmu skaitli: "))
b = float(input("Ievadiet otru skaitli: "))
c = float(input("Ievadiet trešu skaitli: "))

if a < b:
    if a < c:
        print(f"Vismazākais skaitlis ir {a}")
    else: 
        print(f"Vismazākais skaitlis ir {c}")
else: 
    if b < c:
        print(f"Vismazākais skaitlis ir {b}")
    else: 
        print(f"Vismazākais skaitlis ir {c}")