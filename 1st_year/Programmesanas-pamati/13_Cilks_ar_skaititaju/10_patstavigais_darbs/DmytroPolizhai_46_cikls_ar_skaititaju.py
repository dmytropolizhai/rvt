"""
Visvienkāršākā programma ar ciklu for
Izvada: skaitļus no 10 līdz 0 (0 ieskaitot) ar soli -1

Izveidoja: Dmytro Polizhai
"""
from time import sleep

for x in range(10, 0, -1):
    print(x, end="\t", flush=True)
    sleep(1)