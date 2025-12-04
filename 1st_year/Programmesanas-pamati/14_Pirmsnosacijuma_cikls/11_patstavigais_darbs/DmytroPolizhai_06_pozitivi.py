"""
Lietotājam liek ievadīt pozitīvus skaitļus vai nulli un izrēķina ievadīto skaitļu un nulles skaitu. 
Skaitļa ievadi beidz, kad tiek ievadīts negatīvs skaitlis
Izveidoja: Dmytro Polizhai
"""

# 1 variants
n = float(input("Ievadiet skaitli: "))
count = 0

while n >= 0:
    count += 1
    n = float(input("Ievadiet skaitli: "))

print(count)


# 2 variants
# n = float(input("Ievadiet skaitli: "))
# count = 1

# while n >= 0:
#     n = float(input("Ievadiet skaitli: "))
#     if n >= 0:
#         count += 1

# print(count)
