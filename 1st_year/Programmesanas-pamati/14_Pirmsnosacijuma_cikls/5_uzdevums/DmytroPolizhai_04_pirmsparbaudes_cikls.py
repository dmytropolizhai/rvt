"""
Izdoma savu piemēru no dzīves ar pirmspārbaudes ciklu un apraksti to skriptā ar ciklu while. 
(ja pēkšņi programmas kods sakritīs ar kursa biedra kodu (norakstīsi), tad pildīsi citus 3 individuālus uzdevumus).
Izveidoja: Dmytro Polizhai
"""

MAX_MONEY_PER_SESSION = 1000

money_to_withdraw = float(input("Cik daudz naudas izņemt: "))

print(f"Tu ievadīji {money_to_withdraw}")

while 0 <= money_to_withdraw < 1000:
    if money_to_withdraw <= 0:
        print("Naudas nevar būt negatīvi vai vienāds ar 0")
    elif money_to_withdraw > MAX_MONEY_PER_SESSION:
        print("Tik daudz naudas par vienu sesīju Jūs nevarāt izņemt")
    else:
        break

    money_to_withdraw = float(input("Cik daudz naudas izņemt: "))

print(f"Sekmīgi ir izņemts no bankomāta: {money_to_withdraw}")