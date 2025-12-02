from random import randint 

print("Datorspēle \nUzmini skaitli.")
print('Dators "iedomājas" veselo skaitli no 1 līdz 10. \n')
print('Uzminiet skaitli.')

computer_number: int = randint(1, 10)

while True:
    try:
        inp = int(input("Ievadiet skaitli no 1 līdz 10, ieskaitot 10: "))

        if computer_number < inp:
            print("Neuzminējāt. Ievadiet mazāku skaitli.")
        elif computer_number > inp:
            print("Neuzminējāt. Ievadiet lielāku skaitli.")
        else:
            break
    except:
        continue

print("Uzminējāt!!!")

    
