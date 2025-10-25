"""
Uzdevums. Jums ir administratora panelis, un jums jāpārbauda, ​​vai lietotājs ir pieteicies un vai lietotājs ir administrators.
"""
is_logged = str(input("Vai lietotājs ir logged? [y/n]: ")) 

if is_logged.lower() == "y":
    is_admin = str(input("Vai lietotājs ir admin? [y/n]: "))
    
    if is_admin:
        print("Tu esi admins!")    
    
    else:
        print("Tu esi pats cilvēks!")