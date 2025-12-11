"""
Lietotājam liek ievadīt pozitīvus skaitļus vai nulli un izrēķina ievadīto skaitļu un nulles skaitu. 
Skaitļa ievadi beidz, kad tiek ievadīts negatīvs skaitlis. 

2. variants ar 2 salīdzinājumiem un loģisku operāciju.

Izveidoja: Dmytro Polizhai
"""

zero_count = 0
positive_count = 0

n = float(input("Ievadi skaitli: "))

while n >= 0:
    if n > 0: 
        positive_count += 1
    elif n == 0:
        zero_count += 1

    n = float(input("Ievadi skaitli: "))
    
print("Pozitīvo skaitļu skaits:", positive_count)
print("Nulles skaits:", zero_count)