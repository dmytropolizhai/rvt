"""
10. uzdevums

Aprēķina n pēc kārtas ņemtu skaitļu summu. Intervāla sākumu un n ievada lietotājs. 
Piemēram, ja intervāla sākums ir 6 un n ir 4, tad saskaita 6+7+8+9=30. 

Izveidoja: Dmytro Polizhai
"""

start = int(input("Ievadiet sākumu veselo skaitli: "))
n = int(input("Ievadiet cik daudz skaitļu: "))

sum_ = 0
stop = start + n

for i in range(start, stop):
    # Ja skaitlis ir pedējais, tad rakstām "=" zīme, lai pabeigtu atrasinājumu
    if i == stop - 1:
        print(i, end="=")
    else:
        print(i, end="+")
        
    sum_ += i

print(sum_)