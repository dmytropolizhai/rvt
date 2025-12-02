"""
Pieprasa ievadīt lietotāja statusu un parbauda, ​​vai lietotājs ir pieteicies un vai lietotājs ir administrators, izmanotojot iekļautus nosacījumus.
Izveidoja: Dmytro Polizhai
"""

is_logged = str(input("Vai lietotājs ir pieteicies? [y/n]: ")) 

if is_logged.lower() == "y":
    is_admin = str(input("Vai lietotājs ir administrators? [y/n]: "))
    
    if is_admin.lower() == "y":
        print("Tu esi admins!")    
    
    else:
        print("Tu esi pats cilvēks!")