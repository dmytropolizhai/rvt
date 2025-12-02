subtotal = float(input("Ievadiet pirkuma summu: "))
discount = 0.11


if subtotal >= 50:
    subtotal_discount = subtotal * discount
else: 
    subtotal_discount = 0


total = subtotal - subtotal_discount

print(f"Summa bez atlaides: {subtotal}\nAtlaide eiro: {subtotal_discount}\nSumma ar atlaidi: {total} ")