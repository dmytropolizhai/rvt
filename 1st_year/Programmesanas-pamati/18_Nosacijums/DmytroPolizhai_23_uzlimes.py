from math import trunc
from decimal import Decimal

STICKER_PRICE = 9 # Cena par vienu uzlīmi


bill = Decimal(input("Ievadiet čeka summu: ")) # Ievadu dati
sticker_count = 0 # Uzlīmes daudzums

if bill >= STICKER_PRICE: # Vai čeka summa ir lielāks nekā cenas par vienu uzlīmi
    print("Jums ir uzlīmes")
    sticker_count: int = trunc(bill // STICKER_PRICE) # Formula, lai uzzinātu uzlīmes dauzdumu (jābūt vesels skaitlis)
else: # citādi
    print("Jums NAV uzlīmes")

print(sticker_count) # Izvadām uzlīmes daudzumu 
