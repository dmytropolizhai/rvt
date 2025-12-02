"""
Pieprasa ievadīt lietotāja statusu un parbauda, ​​vai lietotājs ir pieteicies un vai lietotājs ir administrators, izmanotojot loģisku operatoru "and".
Izveidoja: Dmytro Polizhai
"""

is_logged = str(input("Vai lietotājs ir pieteicies? [y/n]: ")) 
is_admin = str(input("Vai lietotājs ir administrators? [y/n]: "))

if is_logged.lower() == "y" and is_admin:
    print("Tu esi admins!")    
    
else:
    print("Tu esi pats cilvēks!")