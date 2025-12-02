"""
Naudas summa 100 eiro bankā pēc 3 gadiem uz 9 procentiem gadā

Izveidoja: Dmytro Polizhai
"""

sum_ = 100

for y in range(1, 4):
    sum_ += sum_ * 0.09

print(sum_)