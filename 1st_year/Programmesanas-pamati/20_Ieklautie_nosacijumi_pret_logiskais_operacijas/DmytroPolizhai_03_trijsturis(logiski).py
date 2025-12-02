"""
Pieprasa ievadīt trīs malas garumu un parbauda, vai ir iespēja uzzīmēt trijsturu ar ievadītām malām, izmantojot loģisku operatoru "and".
Izveidoja: Dmytro Polizhai
"""


a = float(input("Ievadiet 1. malu: "))
b = float(input("Ievadiet 2. malu: "))
c = float(input("Ievadiet 3. malu: "))

if a < (b + c) and b < (a + c) and c < (a + b):
    print("Jums ir iespēja uzzīmēt trijstūri")
else:
    print("Jums nav iespējas uzzīmēt trijstūri")