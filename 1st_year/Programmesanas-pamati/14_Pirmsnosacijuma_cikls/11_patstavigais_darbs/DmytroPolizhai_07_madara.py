"""
Madaras tēvs  ieguldīja naudas summa 800 eiro bankā uz 5 gadiem uz 7 procentiem gadā.
Izskaitļo katra gada summu un izvadā arī kopējo summu par 5 gadiem.
Izveidoja: Dmytro Polizhai
"""

START_SUM = 800
YEARS = 5
PROCENTAGE = 0.07

year = 1
sum_with_percentage = START_SUM

while year <= YEARS:
    sum_with_percentage += sum_with_percentage * PROCENTAGE
    year += 1

print(sum_with_percentage)