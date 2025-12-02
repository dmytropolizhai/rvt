"""
5. uzdevums

Naudas summa 100 eiro bankā pēc 3 gadiem uz 9 procentiem gadā

Izveidoja: Dmytro Polizhai
"""

sum_after_3_years = 100

for i in range(1, 4):
    sum_after_3_years += sum_after_3_years * 0.09
    
print("Summa 100 eiro pēc 3 gadiem uz 9 procentiem gadā būs", sum_after_3_years)