'''
Programma nosaka vai vesels skaitlis ir nepārs vai pārs.
Dalām skaitli ar 2 un atlikumu salīdzinām ar 0.
Atlikums ir 0, tad pārs; atlikums ir 1, - nepāra

Izveidoja: Dmytro Polizhai
'''

vesels_skaitlis = int(input("Ievadiet veselo skaitli: "))
if vesels_skaitlis % 2 != 0:
    print(f"Skaitlis {vesels_skaitlis} ir nepāra")
else:
    print(f"Skaitlis {vesels_skaitlis} ir pāra")