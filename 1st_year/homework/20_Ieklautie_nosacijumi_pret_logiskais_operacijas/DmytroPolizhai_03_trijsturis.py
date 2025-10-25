a = float(input("Ievadiet 1. malu: "))
b = float(input("Ievadiet 2. malu: "))
c = float(input("Ievadiet 3. malu: "))

if a < b + c:
    if b < a + c:
        if c < a + b:
            print("Jums ir iespēja uzzīmēt trijstūri")
        else:
            print("Jums nav iespējas uzzīmēt trijstūri")
    else:
        print("Jums nav iespējas uzzīmēt trijstūri")
else:
    print("Jums nav iespējas uzzīmēt trijstūri")
