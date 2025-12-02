"""
Pieprasa ievadīt reālo skaitli un parbauda, vai ievadīts skaitlis pieder intervalam [4; 5), izvada pieder vai nepieder, izmanotojot iekļautus nosacījumus.
Izveidoja: Dmytro Polizhai
"""


n = float(input("Skaitlis: "))

if n >= 4:
    if n < 5:
        print("n pieder intervālam [4;5)")
    else:
        print("n NEpieder intervālam [4;5)")

else:
    print("n NEpieder intervālam [4;5)")
