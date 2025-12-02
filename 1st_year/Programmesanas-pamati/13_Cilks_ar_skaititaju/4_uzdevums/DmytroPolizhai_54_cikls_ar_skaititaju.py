"""
2. uzdevums

Faktoriāla aprēķināšana n! = 1 ⋅ 2 ⋅ 3 ⋅ … ⋅ (n - 1) ⋅ n

Izveidoja: Dmytro Polizhai
"""

print("Faktoriāla arēķināšana n!")

n = int(input("Ievadiet skaitli: "))
factorial = 1

print(f"{n}! =", end=" ")

for i in range(2, n + 1):
    print(f"{i}", end=" ")
    if i != n:
        print("x", end=" ")
    
    factorial *= i 

print(f"= {factorial}")
