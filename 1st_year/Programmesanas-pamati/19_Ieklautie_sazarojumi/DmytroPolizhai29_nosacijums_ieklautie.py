sister_age = int(input("Ievadiet māsas vecumu: "))
brother_age = int(input("Ievadiet brāļa vecumu: "))

if sister_age != brother_age:
    if brother_age > sister_age:
        print("Vecākais cilvēks ir brālis")
    else:
        print("Vecākais cilvēks ir māsa")
else:
    print("Viņi ir dvīņi.")