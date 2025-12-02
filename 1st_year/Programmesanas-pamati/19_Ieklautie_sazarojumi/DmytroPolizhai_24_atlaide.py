from decimal import Decimal

subtotal = Decimal(input("Ievadiet pirkuma summu: "))

if subtotal >= 50:

    if subtotal >= 70:
        discount = 0.14
    else:
        discount = 0.11

    subtotal_discount = subtotal * Decimal(discount)
else: 
    subtotal_discount = 0 


total = subtotal - subtotal_discount

print(f"Summa bez atlaides: {subtotal}\nAtlaide eiro: {subtotal_discount}\nSumma ar atlaidi: {total} ")