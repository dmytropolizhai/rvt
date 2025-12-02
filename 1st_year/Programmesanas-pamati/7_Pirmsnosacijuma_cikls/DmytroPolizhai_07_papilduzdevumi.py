"""
Faktoriāla aprēķināšana n! = 1 * 2 * 3 * … * (n - 1) * n

Izveidoja: Dmytro Polizhai
"""

n = int(input())

fact = 1
for i in range(2, n + 1, 1):
    fact *= i

print(fact)