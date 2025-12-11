"""
Madaras tēvs  ieguldīja naudas summa 800 eiro bankā uz 5 gadiem uz 7 procentiem gadā.
Izskaitļo katra gada summu un izvadā arī kopējo summu par 5 gadiem.
Izveidoja: Dmytro Polizhai
"""

year = 0
sum_with_percentage = 800

while year <= 5:
    print(f"{year}. gads - {sum_with_percentage} eiro")
    sum_with_percentage += sum_with_percentage * 0.07
    year += 1