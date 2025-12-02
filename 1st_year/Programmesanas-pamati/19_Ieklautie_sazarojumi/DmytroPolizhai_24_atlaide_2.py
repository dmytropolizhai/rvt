subtotal = float(input("Ievadiet pirkuma summu: "))

if subtotal >= 50:
    if subtotal >= 70:
        discount = subtotal * 0.14
    else:
        discount = subtotal * 0.11

    total = subtotal - discount

    print(f"Summa bez atlaides: {subtotal}\nAtlaide eiro: {discount}\nSumma ar atlaidi: {total} ")

else: 
    print(f"Atlaides jums nav: {subtotal}")

