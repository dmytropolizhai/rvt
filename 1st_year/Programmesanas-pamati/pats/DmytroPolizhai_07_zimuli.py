pencil_count_1 = int(input("Ja pērk "))
money_count_1 = int(input("zīmuļus, atliek "))
pencil_count_2 = int(input("Ja pirtu "))
money_count_2 = int(input("zīmuļus "))

price = (money_count_1 + money_count_2) // abs(pencil_count_1 - pencil_count_2)
money = pencil_count_1 * price + money_count_1

print("Zīmuļa cena: ", price)
print("Naudas ir pircējam: ", money)