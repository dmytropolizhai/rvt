"""
Lietotājam liek ievadīt pozitīvus skaitļus vai nulli un izrēķina ievadīto skaitļu un nulles skaitu. 
Skaitļa ievadi beidz, kad tiek ievadīts negatīvs skaitlis

1. variants ar 1 salīdzināšanu

Izveidoja: Dmytro Polizhai
"""

zero_count = 0
positive_count = 0

while True:
    n = float(input("Ievadiet skaitli: "))

    if n > 0:
        positive_count += 1
    elif n == 0:
        zero_count += 1
    else: # ja ir ievadīts negatīvais skaitlis
        break # keyword, lai beigtu ciklu (ir izmantots, lai nebūtu mūžīgais cikls)

print("Pozitīvo skaitļu skaits:", positive_count)
print("Nulles skaits:", zero_count)